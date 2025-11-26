import smtplib
from email.message import EmailMessage

# Configuración
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'
EMAIL_PASS = 'tu_app_password'

def enviar_masivo():
    lista_correos = ['usuario1@ejemplo.com', 'usuario2@ejemplo.com', 'usuario3@ejemplo.com']
    
    msg = EmailMessage()
    msg['Subject'] = 'Notificación General'
    msg['From'] = EMAIL_USER
    # Enviar a todos en el campo 'To' (todos ven los correos de los demás)
    # msg['To'] = ', '.join(lista_correos) 
    
    # MEJOR: Usar copia oculta (Bcc) para privacidad
    msg['To'] = EMAIL_USER # Se envía a uno mismo
    msg['Bcc'] = ', '.join(lista_correos) # Los demás van en copia oculta
    
    msg.set_content('Hola a todos, este es un mensaje masivo.')

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print(f"Enviado a {len(lista_correos)} destinatarios.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    enviar_masivo()
