import os

ruta = os.path.join("carpeta", "archivo.txt")
print(f"Ruta unida: {ruta}")

absoluta = os.path.abspath("3_archivos.py")
print(f"Ruta absoluta: {absoluta}")

print(f"Nombre base: {os.path.basename(absoluta)}")
print(f"Directorio: {os.path.dirname(absoluta)}")
