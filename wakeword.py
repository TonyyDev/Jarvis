import numpy as np
import sounddevice as sd
from openwakeword.model import Model
from scipy.io.wavfile import write


FRECUENCIA_WAKEWORD = 16000
DISPOSITIVO_WAKEWORD = 1

modelo = Model(
    inference_framework="onnx"
)


def esperar_wakeword():

    print("\n Esperando: Hey Jarvis...")

    bloque = 1280

    hablando = False
    silencio = 0

    grabacion = []

    UMBRAL_WAKEWORD = 0.3
    UMBRAL_VOZ = 300
    SILENCIO_MAXIMO = 1.0

    with sd.InputStream(
        samplerate=FRECUENCIA_WAKEWORD,
        blocksize=bloque,
        channels=1,
        dtype="int16",
        device=DISPOSITIVO_WAKEWORD
    ) as stream:

        while True:

            audio, overflow = stream.read(bloque)
            if not hablando:
                print(".", end="", flush=True)
            audio = np.frombuffer(
                audio,
                dtype=np.int16
            )

            # ---------------------------------
            # ESPERANDO "HEY JARVIS"
            # ---------------------------------
            
            if not hablando:

                predicciones = modelo.predict(audio)

                puntuacion = predicciones.get(
                    "hey_jarvis",
                    0
                )

                if puntuacion > UMBRAL_WAKEWORD:

                    print(
                        f"🔥 Hey Jarvis detectado "
                        f"({puntuacion:.2f})"
                    )

                    hablando = True

                continue

            # ---------------------------------
            # YA DETECTAMOS "HEY JARVIS"
            # ---------------------------------

            grabacion.append(audio.copy())

            volumen = np.abs(audio).mean()

            if volumen > UMBRAL_VOZ:

                silencio = 0

                print("Hablando...")

            else:

                silencio += 0.08

                if silencio >= SILENCIO_MAXIMO:

                    break

    if not grabacion:

        print("No se detectó ningún comando.")

        return None

    audio_completo = np.concatenate(
        grabacion,
        axis=0
    )

    archivo = "voz.wav"

    write(
        archivo,
        FRECUENCIA_WAKEWORD,
        audio_completo
    )

    print("Fin de la grabación.")

    return archivo