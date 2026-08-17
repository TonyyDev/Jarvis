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

            if puntuacion > 0.5:

                print(
                    f"🔥 Hey Jarvis detectado "
                    f"({puntuacion:.2f})"
                )

                return True