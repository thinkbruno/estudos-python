from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.download_file import extract_text_from_url
from datetime import datetime

router = APIRouter()


@router.get("/download-text")
def download_text(url: str):
    try:
        file = extract_text_from_url(url)

        filename = f"{datetime.now().strftime('%Y-%m-%d')}_text.txt"

        return StreamingResponse(
            file,
            media_type="text/plain",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
