from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Get User Agent")
async def get_user_agent(request: Request):
    """
    **Get the User-Agent string.**
    """
    ua = request.headers.get("user-agent", "unknown")
    return APIResponse.success(data={"user_agent": ua})
