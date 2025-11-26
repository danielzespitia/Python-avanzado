from docxtpl import DocxTemplate
from docx import Document
import jinja2

# 1. Función filtro
def formato_moneda(valor):
    return f"${valor:,.2f}"

# 2. Crear plantilla
doc = Document()
doc.add_paragraph('Precio: {{ precio | moneda }}')
doc.save('plantilla_filtro.docx')

# 3. Renderizar
doc_tpl = DocxTemplate("plantilla_filtro.docx")
jinja_env = jinja2.Environment()
jinja_env.filters['moneda'] = formato_moneda

doc_tpl.render({'precio': 9876.54321}, jinja_env)
doc_tpl.save("resultado_filtro.docx")
print("Generado: resultado_filtro.docx")
