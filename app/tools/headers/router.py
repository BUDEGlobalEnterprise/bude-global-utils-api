from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Echo Headers")
async def get_headers(request: Request):
    """
    **Echoes back the request headers.**
    """
    return APIResponse.success(data=dict(request.headers))
