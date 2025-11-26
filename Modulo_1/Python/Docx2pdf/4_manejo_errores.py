from docx2pdf import convert

try:
    print("Intentando convertir un archivo inexistente...")
    convert("no_existo.docx")
except FileNotFoundError:
    print(">>> Error capturado: El archivo no se encontró.")
except Exception as e:
    print(f">>> Otro error: {e}")
    print("Nota: Si ves errores de COM/Word, asegúrate de tener Office instalado.")
