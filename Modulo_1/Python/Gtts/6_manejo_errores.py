from gtts import gTTS, gTTSError

try:
    # Intentamos convertir un texto vacío para provocar un error (o simular falta de red)
    # Nota: gTTS a veces valida el texto antes de enviar, así que texto vacío puede lanzar AssertionError o ValueError
    print("Intentando generar audio...")
    tts_error = gTTS(text="Probando errores", lang='es')
    tts_error.save('prueba_error.mp3')
    print("Conversión exitosa.")

except gTTSError as e:
    print(f"Error de conexión con Google TTS: {e}")
except AssertionError as e:
    print(f"Error en los argumentos: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
