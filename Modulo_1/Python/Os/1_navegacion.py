import os

# Obtener directorio actual
cwd = os.getcwd()
print(f"Directorio actual: {cwd}")

# Listar archivos
print("\nArchivos en este directorio:")
for archivo in os.listdir(cwd):
    print(f" - {archivo}")
