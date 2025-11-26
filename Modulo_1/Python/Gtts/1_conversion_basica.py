from gtts import gTTS
import os

# Texto que queremos convertir
texto_basico = "¡Hola! Bienvenido al curso de Python. Esta es una prueba básica de gTTS."

# Crear el objeto gTTS
# lang='es' especifica que el idioma es español
tts_basico = gTTS(text=texto_basico, lang='es')

# Guardar el archivo de audio
archivo_salida = "saludo_basico.mp3"
tts_basico.save(archivo_salida)

print(f"Audio guardado como '{archivo_salida}'")

# Reproducir el audio (Windows)
# os.system(f"start {archivo_salida}")
