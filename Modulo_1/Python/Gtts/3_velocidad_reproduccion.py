from gtts import gTTS
import os

texto_velocidad = "Esta oración se leerá muy despacio para que puedas entender cada palabra."

# Velocidad normal (por defecto)
tts_normal = gTTS(text=texto_velocidad, lang='es', slow=False)
tts_normal.save('velocidad_normal.mp3')

# Velocidad lenta
tts_lento = gTTS(text=texto_velocidad, lang='es', slow=True)
tts_lento.save('velocidad_lenta.mp3')

print("Generado: velocidad_normal.mp3")
print("Generado: velocidad_lenta.mp3")
