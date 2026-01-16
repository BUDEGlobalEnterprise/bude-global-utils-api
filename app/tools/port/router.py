import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_ports():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return {"80": "HTTP"}

@router.get("/", summary="Common Port Lookup")
async def get_port(
    request: Request,
    port: str = Query(..., description="Port Number (e.g. 80)")
):
    """
    **Lookup common service for a port number.**
    """
    ports = get_ports()
    service = ports.get(port, "Unknown Port")
    return APIResponse.success(data={"port": port, "service": service})
