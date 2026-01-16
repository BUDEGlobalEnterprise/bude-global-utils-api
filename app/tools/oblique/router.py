import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_strategies():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("strategies", [])
    except Exception:
        return ["Consult other sources"]

@router.get("/", summary="Oblique Strategies")
async def get_strategy(request: Request):
    """
    **Get a Brian Eno Oblique Strategy.**
    
    Useful for breaking creative blocks.
    """
    strategies = get_strategies()
    strategy = random.choice(strategies)
    return APIResponse.success(data={"strategy": strategy})
