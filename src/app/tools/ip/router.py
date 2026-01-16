from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Get Client IP")
async def get_ip(request: Request):
    """
    **Get the client's IP address.**
    """
    return APIResponse.success(data={
        "ip": request.client.host if request.client else "unknown"
    })
