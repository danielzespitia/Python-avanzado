from docxtpl import DocxTemplate, RichText
from docx import Document

# 1. Crear plantilla
doc = Document()
doc.add_paragraph('Estado: {{ estado }}')
doc.save('plantilla_richtext.docx')

# 2. Renderizar
doc_tpl = DocxTemplate("plantilla_richtext.docx")

rt = RichText()
rt.add('URGENTE', color='#FF0000', bold=True, size=24)
rt.add(' - Revisar ahora', italic=True)

context = {'estado': rt}
doc_tpl.render(context)
doc_tpl.save("resultado_richtext.docx")
print("Generado: resultado_richtext.docx")
