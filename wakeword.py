import numpy as np
import sounddevice as sd
from openwakeword.model import Model


FRECUENCIA_WAKEWORD = 16000
DISPOSITIVO_WAKEWORD = 1

modelo = Model(
    inference_framework="onnx"
)


def esperar_wakeword():

    print("\n🤖 Esperando: Hey Jarvis...")

    bloque = 1280

    grabacion = []

    hablando = False
    silencio = 0

    UMBRAL = 300
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

            audio = np.frombuffer(
                audio,
                dtype=np.int16
            )

            predicciones = modelo.predict(audio)

            puntuacion = predicciones.get(
                "hey_jarvis",
                0
            )

            # Todavía no detectamos Jarvis
            if not hablando:

               
                if puntuacion > 0.3:

                    print(
                        f"🔥 Hey Jarvis detectado "
                        f"({puntuacion:.2f})"
                    )

                    hablando = True

                continue

            # Ya detectamos Hey Jarvis
            volumen = np.abs(audio).mean()

            grabacion.append(audio.copy())

            if volumen > UMBRAL:

                silencio = 0

            else:

                silencio += 0.08

                if silencio >= SILENCIO_MAXIMO:
                    break

    if not grabacion:
        return None

    return np.concatenate(
        grabacion,
        axis=0
    )