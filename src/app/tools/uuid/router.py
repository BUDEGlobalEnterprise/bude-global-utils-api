import uuid
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Generate UUID")
async def generate_uuid(request: Request):
    """
    **Generate a random UUID v4.**
    
    Standard Universally Unique Identifier.
    """
    new_uuid = str(uuid.uuid4())
    return APIResponse.success(data={"uuid": new_uuid})
