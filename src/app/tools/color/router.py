from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

@router.get("/hex-to-rgb", summary="Hex to RGB")
async def hex_to_rgb(
    request: Request,
    hex: str = Query(..., description="Hex code (e.g. #FF0000 or FF0000)")
):
    """
    **Convert Hex color code to RGB.**
    """
    hex = hex.lstrip('#')
    try:
        if len(hex) != 6:
            raise ValueError
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        return APIResponse.success(data={
            "hex": f"#{hex.upper()}",
            "rgb": [r, g, b],
            "css_rgb": f"rgb({r}, {g}, {b})"
        })
    except ValueError:
        return APIResponse.error("Invalid Hex code. Format: #RRGGBB")

@router.get("/rgb-to-hex", summary="RGB to Hex")
async def rgb_to_hex(
    request: Request,
    r: int = Query(..., ge=0, le=255),
    g: int = Query(..., ge=0, le=255),
    b: int = Query(..., ge=0, le=255)
):
    """
    **Convert RGB values to Hex.**
    """
    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b).upper()
    return APIResponse.success(data={
        "rgb": [r, g, b],
        "hex": hex_code
    })
