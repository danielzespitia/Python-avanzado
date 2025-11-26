import smtplib
from email.message import EmailMessage

# Configuración
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'
EMAIL_PASS = 'tu_app_password'
DESTINATARIO = 'destinatario@ejemplo.com'

def enviar_texto():
    msg = EmailMessage()
    msg['Subject'] = 'Reporte Diario'
    msg['From'] = EMAIL_USER
    msg['To'] = DESTINATARIO
    
    cuerpo = """
    Hola equipo,
    
    El proceso de hoy finalizó correctamente.
    No se encontraron errores.
    
    Saludos,
    Bot de Python
    """
    msg.set_content(cuerpo)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print("Correo de texto enviado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    enviar_texto()
