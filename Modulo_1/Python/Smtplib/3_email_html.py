import smtplib
from email.message import EmailMessage

# Configuración
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'
EMAIL_PASS = 'tu_app_password'
DESTINATARIO = 'destinatario@ejemplo.com'

def enviar_html():
    msg = EmailMessage()
    msg['Subject'] = 'Oferta Especial'
    msg['From'] = EMAIL_USER
    msg['To'] = DESTINATARIO

    # Versión texto plano (fallback)
    msg.set_content('¡Hola! Tenemos una oferta especial para ti. Visita nuestra web.')

    # Versión HTML
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:Green;">¡Oferta Especial!</h1>
            <p>Hola,</p>
            <p>No te pierdas nuestros descuentos de temporada.</p>
            <button style="background-color: #4CAF50; color: white; padding: 15px 32px;">
                <a href="https://www.ejemplo.com" style="color: white; text-decoration: none;">Ver Ofertas</a>
            </button>
        </body>
    </html>
    """
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print("Correo HTML enviado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    enviar_html()
