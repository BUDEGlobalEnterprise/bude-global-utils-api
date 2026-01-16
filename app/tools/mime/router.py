import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_mime_types():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {".json": "application/json"}

@router.get("/", summary="MIME Type Lookup")
async def get_mime(
    request: Request,
    ext: str = Query(..., description="File extension with dot (e.g. .json)")
):
    """
    **Lookup MIME type for a file extension.**
    """
    if not ext.startswith("."):
        ext = "." + ext
        
    mimes = get_mime_types()
    mime_type = mimes.get(ext.lower(), "application/octet-stream")
    return APIResponse.success(data={"extension": ext, "mime_type": mime_type})
