import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_jokes():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("jokes", ["I forgot the joke."])
    except Exception:
        return ["I forgot the joke."]

@router.get("/", summary="Random Dad Joke")
async def get_dad_joke(request: Request):
    """
    **Get a random dad joke.**
    """
    jokes = get_jokes()
    joke = random.choice(jokes)
    return APIResponse.success(data={"joke": joke})
