import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_http_codes():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {"200": "OK"}

@router.get("/", summary="HTTP Status Lookup")
async def get_http_status(
    request: Request,
    code: str = Query(..., description="HTTP Status Code (e.g. 404)")
):
    """
    **Lookup description for an HTTP status code.**
    """
    codes = get_http_codes()
    description = codes.get(code, "Unknown Status Code")
    return APIResponse.success(data={"code": code, "description": description})
