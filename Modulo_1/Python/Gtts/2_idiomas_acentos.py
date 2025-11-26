from gtts import gTTS
import gtts.lang
import os

# Listar todos los idiomas disponibles
idiomas = gtts.lang.tts_langs()
print("Algunos idiomas soportados:")
for codigo, nombre in list(idiomas.items())[:10]: # Mostramos solo los primeros 10
    print(f"{codigo}: {nombre}")

print("...\n")

# Ejemplo de acentos en Español
texto_acento = "Hola, ¿cómo estás? Esto es una prueba de acento."

# Español de España
tts_es = gTTS(text=texto_acento, lang='es', tld='es')
tts_es.save('acento_espana.mp3')
print("Generado: Español de España")

# Español de México
tts_mx = gTTS(text=texto_acento, lang='es', tld='com.mx')
tts_mx.save('acento_mexico.mp3')
print("Generado: Español de México")

# Inglés Australiano
tts_au = gTTS(text="Hello mate, how are you doing?", lang='en', tld='com.au')
tts_au.save('acento_australia.mp3')
print("Generado: Inglés Australiano")
