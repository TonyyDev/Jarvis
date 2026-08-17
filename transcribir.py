from faster_whisper import WhisperModel

print("Cargando modelo...")

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

for segmento in segmentos:
    print(segmento.text)

print("Transcripción terminada.")