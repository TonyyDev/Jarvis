import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from ollama import chat
import numpy as np
from wakeword import esperar_wakeword

from herramientas import (
    abrir_youtube,
    abrir_word,
    abrir_excel,
    abrir_google
)


# ─────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────

DURACION = 5
FRECUENCIA = 44100
DISPOSITIVO = 1


# ─────────────────────────────
# HERRAMIENTAS DISPONIBLES PARA QWEN
# ─────────────────────────────

DESCRIPCION_HERRAMIENTAS = """
Eres el cerebro de un asistente llamado Jarvis.

Estas son las herramientas disponibles:

- abrir_youtube: abre YouTube.
- abrir_word: abre Microsoft Word.
- abrir_excel: abre Microsoft Excel.
- abrir_google: abre Google.

Si el usuario quiere realizar una de estas acciones,
responde ÚNICAMENTE con el nombre de la herramienta.

Si no corresponde a ninguna herramienta, responde:
ninguna

No expliques nada.
No escribas frases adicionales.
Devuelve únicamente el nombre de la herramienta.
"""


# ─────────────────────────────
# CARGAR WHISPER
# ─────────────────────────────

print("Cargando Whisper...")

modelo = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("✅ Whisper listo.")


# ─────────────────────────────
# ESCUCHAR
# ─────────────────────────────

def escuchar():

    print("\nEsperando que hables...")

    samplerate = FRECUENCIA
    bloque = int(samplerate * 0.1)

    grabacion = []

    hablando = False
    silencio = 0

    UMBRAL = 300
    SILENCIO_MAXIMO = 1.0

    with sd.InputStream(
        samplerate=samplerate,
        channels=2,
        dtype="int16",
        device=DISPOSITIVO,
        blocksize=bloque
    ) as stream:

        while True:

            audio, overflow = stream.read(bloque)

            volumen = np.abs(audio).mean()

            if volumen > UMBRAL:

                if not hablando:
                    print("Hablando...")

                hablando = True
                silencio = 0

                grabacion.append(audio.copy())

            elif hablando:

                grabacion.append(audio.copy())

                silencio += 0.1

                if silencio >= SILENCIO_MAXIMO:
                    break

    archivo = "voz.wav"

    audio_completo = np.concatenate(
        grabacion,
        axis=0
    )

    write(
        archivo,
        samplerate,
        audio_completo
    )

    print("Fin de la grabación.")

    return archivo
# ─────────────────────────────
# TRANSCRIBIR
# ─────────────────────────────

def transcribir(archivo):

    segmentos, informacion = modelo.transcribe(
        archivo,
        language="es"
    )

    texto = ""

    for segmento in segmentos:
        texto += segmento.text

    return texto.strip()


# ─────────────────────────────
# PREGUNTAR A QWEN
# ─────────────────────────────

def preguntar_ia(texto):

    respuesta = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": DESCRIPCION_HERRAMIENTAS
            },
            {
                "role": "user",
                "content": texto
            }
        ]
    )

    return respuesta["message"]["content"].strip().lower()


# ─────────────────────────────
# EJECUTAR HERRAMIENTA
# ─────────────────────────────

def ejecutar_herramienta(nombre):

    if nombre == "abrir_youtube":
        abrir_youtube()

    elif nombre == "abrir_word":
        abrir_word()

    elif nombre == "abrir_excel":
        abrir_excel()

    elif nombre == "abrir_google":
        abrir_google()

    else:
        print("No reconocí ninguna herramienta.")


# ─────────────────────────────
# JARVIS - Principal
# ─────────────────────────────


print("JARVIS, Está listo. ")


while True:

    esperar_wakeword()

    print("Jarvis activado.")

    archivo = escuchar()

    texto = transcribir(archivo)

    print("Entendí:", texto)

    if not texto:
        continue

    if "salir" in texto.lower():
        print("Jarvis apagándose...")
        break

    herramienta = preguntar_ia(texto)

    print("Qwen eligió:", herramienta)

    ejecutar_herramienta(herramienta)