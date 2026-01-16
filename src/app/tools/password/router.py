import secrets
import string
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Generate Random Password")
async def generate_password(
    request: Request,
    length: int = Query(16, ge=8, le=128, description="Length of password (8-128)")
):
    """
    **Generate a secure random password.**
    
    Uses standard alphanumeric characters + punctuation.
    """
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return APIResponse.success(data={
        "password": password,
        "length": length
    })
