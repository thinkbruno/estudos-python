from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.pdf_generator import generate_pdf_file

router = APIRouter()


@router.get("/generate-pdf")
def generate_pdf():
    data = {"José": "12", "Maria": "20", "Carlos": "14", "Olivia": "31"}

    try:
        pdf_file = generate_pdf_file(data)

        return StreamingResponse(
            pdf_file,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=lista.pdf"},
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
