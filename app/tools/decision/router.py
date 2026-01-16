import random
from fastapi import APIRouter, Query, Request
from app.core.response import APIResponse

router = APIRouter()

@router.get("/coin", summary="Flip a Coin")
async def flip_coin(request: Request):
    """
    **Flip a virtual coin.**
    
    Returns either "Heads" or "Tails".
    """
    result = random.choice(["Heads", "Tails"])
    return APIResponse.success(data={"result": result})

@router.get("/magic-8-ball", summary="Ask the Magic 8-Ball")
async def magic_8_ball(request: Request):
    """
    **Consult the Magic 8-Ball.**
    
    Returns a mystical answer to your yes/no question.
    """
    answers = [
        "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
        "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
        "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "Don't count on it", "My reply is no", "My sources say no",
        "Outlook not so good", "Very doubtful"
    ]
    result = random.choice(answers)
    return APIResponse.success(data={"answer": result})

@router.get("/choice", summary="Random Choice Picker")
async def make_choice(request: Request, options: str = Query(..., description="Comma-separated list of options (e.g. 'Pizza,Sushi,Burger')")):
    """
    **Pick a random option from a list.**
    
    Provide a comma-separated string of options, and this tool will pick one for you.
    """
    choices = [opt.strip() for opt in options.split(",") if opt.strip()]
    if not choices:
        return APIResponse.error("No valid options provided")
    
    result = random.choice(choices)
    return APIResponse.success(data={"choice": result})
