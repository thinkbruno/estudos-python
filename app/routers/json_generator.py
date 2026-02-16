from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.json_generator import generate_json_file

router = APIRouter()


@router.get("/json-generator")
def json_generator():
    file = generate_json_file()

    return StreamingResponse(
        file,
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=data.json"},
    )
