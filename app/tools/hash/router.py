import hashlib
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

@router.get("/", summary="Generate Hashes")
async def generate_hash(request: Request, text: str = Query(..., description="Text to hash")):
    """
    **Generate SHA256 and MD5 hashes for the input text.**
    """
    sha256 = hashlib.sha256(text.encode("utf-8")).hexdigest()
    md5 = hashlib.md5(text.encode("utf-8")).hexdigest()
    
    return APIResponse.success(data={
        "input": text,
        "sha256": sha256,
        "md5": md5
    })
