from fastapi import APIRouter, HTTPException
from app.services.battery import get_battery_percent, BatteryNotFoundError

router = APIRouter(prefix="/battery", tags=["Battery"])

@router.get("/")
def battery_status():
    try:
        percent = get_battery_percent()
        return {"battery_percent": percent}
    except BatteryNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
