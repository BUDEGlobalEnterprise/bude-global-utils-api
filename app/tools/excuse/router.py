import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_excuses():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r") as f:
            data = json.load(f)
            return data.get("excuses", [])
    except Exception:
        return ["It deferred compilation", "The cloud is down"]

@router.get("/", summary="Get a Developer Excuse")
async def get_excuse(request: Request):
    """
    **Get a specific, professional-sounding excuse.**
    
    Returns a random developer excuse like "It works on my machine" or "DNS propagation issue".
    """
    excuses = get_excuses()
    excuse = random.choice(excuses)
    return APIResponse.success(data={"excuse": excuse})
