from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO


def generate_pdf_file(data: dict) -> BytesIO:
    try:
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)

        width, height = A4
        y = height - 50

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(200, y, "Lista de nomes")

        y -= 30
        pdf.setFont("Helvetica", 12)

        for name, age in data.items():
            pdf.drawString(200, y, f"{name} : {age}")
            y -= 20

        pdf.save()
        buffer.seek(0)

        return buffer

    except Exception:
        raise ValueError("Erro ao gerar PDF")
