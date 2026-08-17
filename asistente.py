from faster_whisper import WhisperModel
import webbrowser


def abrir_youtube():
    webbrowser.open("https://www.youtube.com")
    print("YouTube abierto correctamente.")


modelo = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Transcribiendo...")

segmentos, informacion = modelo.transcribe(
    "voz.wav",
    language="es"
)

texto = ""

for segmento in segmentos:
    texto += segmento.text

print("Entendí:", texto)

if "youtube" in texto.lower():
    abrir_youtube()
else:
    print("No reconocí ningún comando.")