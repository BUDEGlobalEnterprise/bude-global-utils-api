import random
import json
from pathlib import Path
from fastapi import APIRouter, Request, Query
from app.core.response import APIResponse

router = APIRouter()

def get_lorem_sentences():
    try:
        data_path = Path(__file__).parent / "data.json"
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("sentences", ["Lorem ipsum."])
    except Exception:
        return ["Lorem ipsum."]

@router.get("/", summary="Lorem Ipsum Generator")
async def get_lorem(
    request: Request,
    sentences: int = Query(3, ge=1, le=10, description="Number of sentences (1-10)")
):
    """
    **Generate random Lorem Ipsum text.**
    """
    all_sentences = get_lorem_sentences()
    # Random sample allowing replacement if requested > available is strictly not needed as sample > population fails
    # But usually sample w/o replacement is cleaner for text.
    # Our data has 15, max req is 10.
    selected = random.sample(all_sentences, min(sentences, len(all_sentences)))
    text = " ".join(selected)
    
    return APIResponse.success(data={
        "sentences": sentences,
        "text": text
    })
