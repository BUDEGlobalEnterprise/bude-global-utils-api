import random
import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_zen_lines():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("lines", [])
    except Exception:
        return ["Readability counts."]

@router.get("/", summary="Zen of Python")
async def get_zen(
    request: Request,
    all: bool = Query(False, description="Return all lines if true")
):
    """
    **Get lines from The Zen of Python.**
    """
    lines = get_zen_lines()
    if all:
        return APIResponse.success(data={"lines": lines})
    
    line = random.choice(lines)
    return APIResponse.success(data={"line": line})
