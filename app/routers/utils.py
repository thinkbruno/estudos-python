from fastapi import APIRouter
from app.services.password import generate_password

router = APIRouter(prefix="/utils", tags=["Utils"])

@router.get("/password")
def get_password(length: int = 8):
    return {"password": generate_password(length)}
