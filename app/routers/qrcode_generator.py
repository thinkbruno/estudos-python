from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.qrcode_generator import generate_qrcode_image

router = APIRouter()


@router.get("/generate-qrcode")
def generate_qrcode(url: str):
    try:
        image = generate_qrcode_image(url)

        return StreamingResponse(image, media_type="image/png")

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
