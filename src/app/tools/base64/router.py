import base64
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

@router.get("/encode", summary="Base64 Encode")
async def encode_base64(request: Request, text: str = Query(..., description="Text to encode")):
    """
    **Encode text to Base64.**
    """
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    return APIResponse.success(data={"input": text, "encoded": encoded})

@router.get("/decode", summary="Base64 Decode")
async def decode_base64(request: Request, encoded: str = Query(..., description="Base64 string to decode")):
    """
    **Decode Base64 to text.**
    """
    try:
        decoded = base64.b64decode(encoded).decode("utf-8")
        return APIResponse.success(data={"input": encoded, "decoded": decoded})
    except Exception:
        return APIResponse.error("Invalid base64 string")
