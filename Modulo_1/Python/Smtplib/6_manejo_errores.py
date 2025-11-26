import smtplib
from email.message import EmailMessage

# Configuración
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'
EMAIL_PASS = 'tu_app_password' # Intenta poner una contraseña incorrecta para probar

def probar_errores():
    msg = EmailMessage()
    msg['Subject'] = 'Test Error'
    msg['From'] = EMAIL_USER
    msg['To'] = 'destino@ejemplo.com'
    msg.set_content('Test')

    try:
        print("Conectando...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.set_debuglevel(1) # Ver detalles de la conexión
            smtp.starttls()
            print("Autenticando...")
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print("Éxito.")
            
    except smtplib.SMTPAuthenticationError:
        print("\n>>> ERROR: Falló la autenticación. Verifica usuario y contraseña.")
    except smtplib.SMTPConnectError:
        print("\n>>> ERROR: No se pudo conectar al servidor.")
    except Exception as e:
        print(f"\n>>> ERROR INESPERADO: {e}")

if __name__ == '__main__':
    probar_errores()
