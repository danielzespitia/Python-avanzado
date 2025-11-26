import os

# Leer variable de entorno
usuario = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"Usuario del sistema: {usuario}")

# Crear variable temporal
os.environ['MI_APP_MODE'] = 'DEV'
print(f"Modo: {os.environ.get('MI_APP_MODE')}")
