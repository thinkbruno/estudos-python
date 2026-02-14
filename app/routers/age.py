from fastapi import APIRouter, HTTPException
from app.services.age import calculate_age_detailed

router = APIRouter(prefix="/age", tags=["Age"])

@router.get("/calculate")
def get_age(birth_date: str):
    try:
        result = calculate_age_detailed(birth_date)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
