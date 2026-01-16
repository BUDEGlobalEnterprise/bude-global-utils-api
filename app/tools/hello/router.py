import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_greetings():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("greetings", [])
    except Exception:
        return [{"lang": "English", "text": "Hello World"}]

@router.get("/", summary="Hello World")
async def get_hello(request: Request):
    """
    **Get 'Hello World' in a random language (human or code).**
    """
    greetings = get_greetings()
    greeting = random.choice(greetings)
    return APIResponse.success(data=greeting)
