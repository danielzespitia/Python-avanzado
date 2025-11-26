import smtplib
from email.message import EmailMessage
import os

# Configuración (Reemplaza con tus datos reales)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'
EMAIL_PASS = 'tu_app_password'
DESTINATARIO = 'destinatario@ejemplo.com'

def enviar_basico():
    msg = EmailMessage()
    msg['Subject'] = 'Prueba Básica'
    msg['From'] = EMAIL_USER
    msg['To'] = DESTINATARIO
    msg.set_content('Hola, esto es una prueba de conexión básica.')

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print("Correo enviado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    enviar_basico()
