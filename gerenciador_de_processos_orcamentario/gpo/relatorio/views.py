from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import os.path

logo_site = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/image/logo.jpg')


def relatorio_view(request):
    template_name='relatorios.html'
    return render(request, template_name)

def relatorio_de_testes(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="formulario_diaria_interno.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    p.saveState()



    # container for the 'Flowable' objects
    elements = []

    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    p = Table(data, 5 * [0.4 * inch], 4 * [0.4 * inch])
    p.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                           ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                           ('VALIGN', (0, 0), (0, -1), 'TOP'),
                           ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                           ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                           ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                           ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                           ]))

    elements.append(p)
    # write the document to disk





    #p.setTitle("Relatório de Viagem Interno")

    p.setFontSize(9)

    p.drawImage(logo_site, 20, 5, width=42, height=42,
                preserveAspectRatio=True, mask='auto')

    p.setFont
    p.drawString(67, 24, " © 2017 - Gerenciador de Processos Orçamentários")

    p.save()
    return response


def relatorio_viagem_interno():
    pass








