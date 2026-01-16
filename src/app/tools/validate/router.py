import json
from pathlib import Path
from fastapi import APIRouter, Query, Request
from app.core.response import APIResponse

router = APIRouter()

def get_validate_message():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("message", "Valid.")
    except Exception:
        return "Valid."

@router.get("/", summary="Universal Validator")
async def validate_input(request: Request, input: str = Query(..., description="Anything you want to validate")):
    """
    **The Yes Man.**
    
    Validates literally anything you send it. Zero judgment.
    """
    message = get_validate_message()
    return APIResponse.success(data={
        "valid": True,
        "input": input,
        "message": message
    })
