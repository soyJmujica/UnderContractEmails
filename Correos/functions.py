from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

def guardarPDF(template_src,content_dict={}):
	template = get_template(template_src)
	html = template.render(content_dict)
	pisa = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return render(result.getvalue(), content_type='application/pdf')

	return None