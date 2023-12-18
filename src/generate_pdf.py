# PEP8 OK
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas

"""estudo: criação de doc em pdf
"""

def generate_pdf(list):
    try:
        pdf_name = input('Nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(pdf_name))
        x = 720
        for name, age in list.items():
            x -= 20
            pdf.drawString(247, x, '{} : {}'.format(name, age))
        pdf.setTitle(pdf_name)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245, 750, 'Lista de nomes')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(pdf_name))
    except:
        raise ValueError('Erro ao gerar {}.pdf'.format(pdf_name))


list = {"José": '12', "Maria": '20', "Carlos": '14', "Olivia": '31'}

generate_pdf(list)
