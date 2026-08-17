

import sounddevice as sd
from scipy.io.wavfile import write

duracion = 5
frecuencia = 44100
dispositivo = 1

print("Preparado...")
print("Habla durante 5 segundos.")

audio = sd.rec(
    int(duracion * frecuencia),
    samplerate=frecuencia,
    channels=2,
    dtype="int16",
    device=dispositivo
)

sd.wait()

print("Grabación terminada.")

write("voz.wav", frecuencia, audio)

print("Audio guardado como voz.wav")