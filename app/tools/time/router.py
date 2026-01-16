import time
from datetime import datetime, timezone
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Get Current Time")
async def get_current_time(request: Request):
    """
    **Get the current server time in multiple formats.**
    
    Returns ISO 8601, Unix Epoch, and UTC timestamp.
    """
    now = datetime.now(timezone.utc)
    return APIResponse.success(data={
        "iso": now.isoformat(),
        "epoch": int(now.timestamp()),
        "utc_string": now.strftime("%Y-%m-%d %H:%M:%S UTC")
    })
