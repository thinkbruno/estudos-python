from fastapi import APIRouter, HTTPException
from app.services.discover_mobile_operator import get_mobile_operator_info

router = APIRouter()


@router.get("/discover-operator")
def discover_operator(number: str):
    try:
        return get_mobile_operator_info(number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
