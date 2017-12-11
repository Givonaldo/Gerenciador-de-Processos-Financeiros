from django.shortcuts import render
import os.path
from fpdf import FPDF
from django.http import HttpResponse

logo_site = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/image/logo.jpg')
caminho_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'somefilename.pdf')


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

def relatorio_de_testes(request):

    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response



def relatorio_view(request):
    template_name='relatorios.html'
    return render(request, template_name)


def relatorio_viagem_interno():
    pass
