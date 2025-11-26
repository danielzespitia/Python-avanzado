from gtts import gTTS
import io

# Texto a convertir
texto_memoria = "Este audio se generó directamente en la memoria RAM, sin tocar el disco duro."

# Crear objeto gTTS
tts_memoria = gTTS(text=texto_memoria, lang='es')

# Crear un buffer de bytes
mp3_fp = io.BytesIO()

# Escribir el audio en el buffer
tts_memoria.write_to_fp(mp3_fp)

# Mover el puntero al inicio del buffer para leerlo
mp3_fp.seek(0)

print(f"Audio generado en memoria. Tamaño: {len(mp3_fp.getvalue())} bytes.")
print("Este objeto 'mp3_fp' podría enviarse por red o reproducirse sin guardar en disco.")
