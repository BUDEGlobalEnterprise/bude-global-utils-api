import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_synergy_phrases():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("phrases", [])
    except Exception:
        return ["Synergize the synergy."]

@router.get("/", summary="Corporate Speak Generator")
async def get_synergy(request: Request):
    """
    **Generate a random corporate buzzword phrase.**
    
    Useful for filling slide decks or impressing management.
    """
    phrases = get_synergy_phrases()
    phrase = random.choice(phrases)
    return APIResponse.success(data={"phrase": phrase})
