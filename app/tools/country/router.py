import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_countries():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {"US": "United States"}

@router.get("/", summary="Country Code Lookup")
async def get_country(
    request: Request,
    code: str = Query(..., description="2-letter ISO Country Code (e.g. US)")
):
    """
    **Lookup country name by ISO code.**
    """
    countries = get_countries()
    name = countries.get(code.upper(), "Unknown Country Code")
    return APIResponse.success(data={"code": code.upper(), "name": name})
