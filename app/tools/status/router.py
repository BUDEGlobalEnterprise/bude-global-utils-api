import random
import json
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_status_messages():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r") as f:
            data = json.load(f)
            return data.get("messages", [])
    except Exception:
        return ["System operational", "All systems go", "Optimal performance"]

@router.get("/", summary="Get System Status Message")
async def get_status(request: Request):
    """
    **Get a cosmetic system status message.**
    
    Returns a random positive status string like "All systems nominal" or "Infrastructure secure".
    Useful for filler UI elements.
    """
    messages = get_status_messages()
    status = random.choice(messages)
    return APIResponse.success(data={"status": status})
