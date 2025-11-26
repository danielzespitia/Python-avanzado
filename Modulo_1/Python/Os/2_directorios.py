import os

carpeta = "carpeta_demo"

# Crear carpeta
if not os.path.exists(carpeta):
    os.mkdir(carpeta)
    print(f"Carpeta '{carpeta}' creada.")
else:
    print(f"La carpeta '{carpeta}' ya existe.")

# Eliminar carpeta (descomentar para probar)
# os.rmdir(carpeta)
# print("Carpeta eliminada.")
