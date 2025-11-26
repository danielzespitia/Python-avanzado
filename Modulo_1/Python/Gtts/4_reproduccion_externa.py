import os

# Asegúrate de tener un archivo mp3 para probar, por ejemplo 'saludo_basico.mp3'
archivo = "saludo_basico.mp3"

if os.path.exists(archivo):
    print(f"Reproduciendo {archivo}...")
    # En Windows
    os.system(f"start {archivo}")
    
    # En macOS
    # os.system(f"afplay {archivo}")

    # En Linux
    # os.system(f"mpg321 {archivo}")
else:
    print(f"El archivo {archivo} no existe. Ejecuta primero 1_conversion_basica.py")
