"""
Ejercicio: Mi Primer Audio-Saludo con Python
"""

# 2. Importar la librería gTTS
from gtts import gTTS

# 3. Texto a convertir en voz
texto_a_voz = "Hola, estoy aprendiendo a convertir texto a voz con Python. ¡Es genial!"

# 4. Crear el objeto gTTS, especificando el texto y el idioma (español)
#    - text: La cadena de texto que queremos convertir.
#    - lang: El código del idioma. 'es' para español.
print("Generando audio a partir del texto...")
tts = gTTS(text=texto_a_voz, lang='es')

# 5. Guardar el audio en un archivo MP3
nombre_archivo = "1.1 saludo.mp3"
tts.save(nombre_archivo)

# 6. Confirmar que el archivo ha sido creado
print(f"¡Éxito! ✅ El archivo de audio '{nombre_archivo}' ha sido creado.")
print("Búscalo en la misma carpeta donde ejecutaste este script. ¡Abre y escucha tu creación! 🎧")
