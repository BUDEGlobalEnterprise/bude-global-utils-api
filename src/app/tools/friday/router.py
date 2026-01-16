import json
from datetime import datetime
from pathlib import Path
from fastapi import APIRouter, Request
from app.core.response import APIResponse

router = APIRouter()

def get_friday_messages():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {"friday_msg": "Read-only Friday.", "other_msg": "Go ahead."}

@router.get("/", summary="Is it Friday?")
async def check_friday(request: Request):
    """
    **Check if today is Friday.**
    
    Returns whether you should deploy or not.
    """
    messages = get_friday_messages()
    # Check if today is Friday (4 = Friday in Python weekday() where Mon=0)
    # Wait, 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun
    is_friday = datetime.now().weekday() == 4
    
    message = messages.get("friday_msg") if is_friday else messages.get("other_msg")
    
    return APIResponse.success(data={
        "is_it_friday": is_friday,
        "should_deploy": not is_friday,
        "message": message
    })
