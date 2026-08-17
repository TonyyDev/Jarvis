from ollama import chat

from herramientas import (
    abrir_youtube,
    abrir_word,
    abrir_excel,
    abrir_google
)


herramientas = """
Estas son las herramientas disponibles:

- abrir_youtube: abre YouTube.
- abrir_word: abre Microsoft Word.
- abrir_excel: abre Microsoft Excel.
- abrir_google: abre Google.

Si el usuario quiere realizar una de estas acciones,
responde ÚNICAMENTE con el nombre de la herramienta.

Si no corresponde a ninguna herramienta, responde:
ninguna
"""


def preguntar_ia(texto):

    respuesta = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": herramientas
            },
            {
                "role": "user",
                "content": texto
            }
        ]
    )

    return respuesta["message"]["content"].strip().lower()


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
        print("quieroNo hay una herramienta para esa petición.")


texto = input("Tú: ")

resultado = preguntar_ia(texto)

print("Qwen eligió:", resultado)

ejecutar_herramienta(resultado)