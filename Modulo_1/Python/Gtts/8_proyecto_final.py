from gtts import gTTS
import os

# Lista de frases con su configuración de idioma y acento
frases = [
    {"texto": "Hola amigo, ¿cómo estás?", "lang": "es", "tld": "com.mx", "archivo": "saludo_mx.mp3"},
    {"texto": "Good morning, have a nice day.", "lang": "en", "tld": "us", "archivo": "saludo_us.mp3"},
    {"texto": "Bonjour tout le monde.", "lang": "fr", "tld": "fr", "archivo": "saludo_fr.mp3"},
    {"texto": "Guten Tag! Wie geht es Ihnen?", "lang": "de", "tld": "de", "archivo": "saludo_de.mp3"}
]

# Crear carpeta de salida si no existe
carpeta_salida = "audios_multilingues"
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

print(f"Generando audios en la carpeta '{carpeta_salida}'...\n")

for item in frases:
    try:
        print(f"Procesando: {item['texto']} ({item['lang']})")
        
        # Crear objeto gTTS
        tts = gTTS(text=item['texto'], lang=item['lang'], tld=item['tld'])
        
        # Ruta completa
        ruta_archivo = os.path.join(carpeta_salida, item['archivo'])
        
        # Guardar
        tts.save(ruta_archivo)
        print(f" -> Guardado en: {ruta_archivo}")
        
    except Exception as e:
        print(f" -> Error procesando '{item['texto']}': {e}")

print("\n¡Proceso completado!")
