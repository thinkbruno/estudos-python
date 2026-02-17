from fastapi import APIRouter, HTTPException
from app.services.speedtest_service import run_speedtest

router = APIRouter()


@router.get("/speedtest")
def speedtest():
    try:
        return run_speedtest()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
