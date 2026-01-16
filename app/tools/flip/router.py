import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_flips():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {"table_flip": "(╯°□°）╯︵ ┻━┻"}

@router.get("/", summary="Table Flip")
async def flip_table(
    request: Request,
    fix: bool = Query(False, description="Set to true to fix the table back")
):
    """
    **Flip a table.**
    
    Or fix it if you are feeling calm.
    """
    flips = get_flips()
    action = flips.get("table_fix") if fix else flips.get("table_flip")
    return APIResponse.success(data={"action": action})
