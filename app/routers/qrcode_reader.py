from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.qrcode_reader import read_qrcode_image

router = APIRouter()


@router.post("/read-qrcode")
async def read_qrcode(file: UploadFile = File(...)):
    try:
        content = await file.read()
        result = read_qrcode_image(content)

        return {"content": result}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
