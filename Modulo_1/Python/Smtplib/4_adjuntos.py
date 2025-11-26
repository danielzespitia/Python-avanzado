import smtplib
from email.message import EmailMessage
import mimetypes
import os

# Configuración
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'
EMAIL_PASS = 'tu_app_password'
DESTINATARIO = 'destinatario@ejemplo.com'

def enviar_adjunto(ruta_archivo):
    msg = EmailMessage()
    msg['Subject'] = 'Envío de Documento'
    msg['From'] = EMAIL_USER
    msg['To'] = DESTINATARIO
    msg.set_content('Adjunto el archivo solicitado.')

    # Detectar tipo MIME
    ctype, encoding = mimetypes.guess_type(ruta_archivo)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    
    maintype, subtype = ctype.split('/', 1)

    try:
        with open(ruta_archivo, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(ruta_archivo)
            
            msg.add_attachment(file_data, 
                               maintype=maintype, 
                               subtype=subtype, 
                               filename=file_name)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print(f"Correo con {file_name} enviado.")
            
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Crear archivo dummy para probar
    with open('reporte.txt', 'w') as f:
        f.write('Datos del reporte...')
        
    enviar_adjunto('reporte.txt')
