import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

# 1. Configuración Mínima
# Django normalmente usa un archivo settings.py, pero aquí lo configuramos en vivo.
if not settings.configured:
    settings.configure(
        DEBUG=True,  # Modo depuración activado
        SECRET_KEY='una-clave-secreta-muy-segura',  # Necesario para seguridad
        ROOT_URLCONF=__name__,  # Indica que las URLs están en este mismo archivo
        ALLOWED_HOSTS=['*'],
    )

# 2. La Vista (View)
# Esta función recibe la petición (request) y devuelve una respuesta.
def vista_hola_mundo(request):
    html = """
    <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #2c3e50; }
                p { color: #7f8c8d; }
            </style>
        </head>
        <body>
            <h1>¡Hola Mundo desde Django!</h1>
            <p>Este es un ejemplo minimalista ejecutado en un solo archivo.</p>
            <p>Django es genial 🚀</p>
        </body>
    </html>
    """
    return HttpResponse(html)

# 3. Las URLs
# Definimos qué URL llama a qué vista.
urlpatterns = [
    path('', vista_hola_mundo),  # La ruta raíz ('') llama a vista_hola_mundo
    path('saludo/', vista_hola_mundo), # La ruta /saludo/ también llama a la misma vista
]

# 4. Ejecución
# Esto permite correr el script como si fuera manage.py
# Ejecutar en terminal: python 1_ejemplo_minimalista.py runserver
if __name__ == "__main__":
    execute_from_command_line(sys.argv)
