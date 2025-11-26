from docx2pdf import convert
import os
from docx import Document
import shutil

# 1. Preparar carpeta con archivos
carpeta = "lote_docs"
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
    
    # Crear un archivo base
    doc = Document()
    doc.add_paragraph('Contenido de prueba.')
    doc.save('base.docx')
    
    # Duplicarlo
    for i in range(3):
        shutil.copy('base.docx', os.path.join(carpeta, f'doc_{i}.docx'))
    os.remove('base.docx')

# 2. Convertir carpeta entera
print(f"Convirtiendo todos los archivos en '{carpeta}'...")
convert(carpeta)
print("¡Conversión por lotes finalizada!")
