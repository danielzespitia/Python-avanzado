from gtts import gTTS
import os

# Crear un archivo de texto de prueba
contenido_libro = """
Capítulo 1: El comienzo.
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.
"""

with open('quijote_breve.txt', 'w', encoding='utf-8') as f:
    f.write(contenido_libro)

# Leer el archivo y convertirlo a audio
with open('quijote_breve.txt', 'r', encoding='utf-8') as f:
    texto_leido = f.read()

# Reemplazar saltos de línea para que la lectura sea más fluida si es necesario
texto_leido = texto_leido.replace('\n', ' ')

tts_libro = gTTS(text=texto_leido, lang='es', tld='es')
tts_libro.save('audiolibro.mp3')

print("Audiolibro generado: audiolibro.mp3")
