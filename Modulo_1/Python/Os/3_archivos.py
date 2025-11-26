import os

archivo = "test.txt"
archivo_nuevo = "test_renombrado.txt"

# Crear archivo
with open(archivo, 'w') as f:
    f.write("Hola")
print("Archivo creado.")

# Renombrar
if os.path.exists(archivo):
    os.rename(archivo, archivo_nuevo)
    print("Archivo renombrado.")

# Eliminar
if os.path.exists(archivo_nuevo):
    os.remove(archivo_nuevo)
    print("Archivo eliminado.")
