import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_shrug_emoji():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("emoji", "¯\\_(ツ)_/¯")
    except Exception:
        return "¯\\_(ツ)_/¯"

@router.get("/", summary="Get Shrug Emoji")
async def get_shrug(request: Request):
    """
    **Get the classic Shrug emoji.**
    
    Returns `¯\\_(ツ)_/¯` so you don't have to escape it yourself.
    """
    emoji = get_shrug_emoji()
    return APIResponse.success(data={"emoji": emoji})
