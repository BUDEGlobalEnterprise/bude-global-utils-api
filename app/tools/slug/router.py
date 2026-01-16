import re
import unicodedata
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def slugify(value, allow_unicode=False):
    """
    Django's slugify logic converted to simple function.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")

@router.get("/", summary="Generate Slug")
async def generate_slug(request: Request, text: str = Query(..., description="Text to slugify")):
    """
    **Convert text to a URL-friendly slug.**
    
    e.g. "Hello World!" -> "hello-world"
    """
    slug = slugify(text)
    return APIResponse.success(data={
        "input": text,
        "slug": slug
    })
