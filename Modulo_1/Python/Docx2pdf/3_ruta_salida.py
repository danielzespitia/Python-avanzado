from docx2pdf import convert
import os
from docx import Document

# 1. Crear archivo
if not os.path.exists('entrada.docx'):
    doc = Document()
    doc.add_paragraph('Texto de prueba.')
    doc.save('entrada.docx')

# 2. Convertir con nombre específico
salida = "mi_archivo_final.pdf"
print(f"Convirtiendo 'entrada.docx' a '{salida}'...")
convert("entrada.docx", salida)
print("¡Hecho!")
