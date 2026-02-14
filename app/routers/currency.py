from fastapi import APIRouter, HTTPException
from app.services.currency import (
    convert_usd_to_brl,
    CurrencyConversionError
)

router = APIRouter(prefix="/currency", tags=["Currency"])


@router.get("/usd-to-brl")
def usd_to_brl(amount: float):
    try:
        result = convert_usd_to_brl(amount)
        return {"usd": amount, "brl": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except CurrencyConversionError as e:
        raise HTTPException(status_code=503, detail=str(e))
