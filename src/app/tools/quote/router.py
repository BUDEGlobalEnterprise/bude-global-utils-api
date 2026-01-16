import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_quotes():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("quotes", [])
    except Exception:
        return [{"text": "Talk is cheap.", "author": "Unknown"}]

@router.get("/", summary="Random Quote")
async def get_quote(request: Request):
    """
    **Get an inspirational tech quote.**
    """
    quotes = get_quotes()
    quote = random.choice(quotes)
    return APIResponse.success(data=quote)
