import json
from pathlib import Path
from fastapi import APIRouter, Response, Request
from app.core.response import APIResponse

router = APIRouter()

def get_teapot_data():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {"error": "I'm a teapot"}

@router.get("/", summary="I'm a Teapot")
async def brew_coffee(request: Request):
    """
    **RFC 2324 Compliance Endpoint.**
    
    Refuses to brew coffee because it is a teapot.
    Returns HTTP 418.
    """
    data = get_teapot_data()
    return APIResponse.error(
        message=data.get("error"),
        code=418,
        details=data.get("type")
    )
