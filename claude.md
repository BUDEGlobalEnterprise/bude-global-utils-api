# Bude Utils API

> A lightweight, stateless utility API by Bude Global Enterprise.

## Project Overview

This is a FastAPI-based REST API providing 62+ stateless utility endpoints for developers. No database, no authentication, no tracking. Just useful tools.

**Live endpoints:** Each tool is independent, stateless, and requires no persistent storage.

## Architecture

```
app/
├── main.py           # FastAPI app, router registration
├── core/
│   ├── config.py     # Settings (PROJECT_NAME, VERSION)
│   └── response.py   # Standardized API response wrapper
├── middleware/
│   ├── caching.py    # Response caching middleware
│   └── enrichment.py # Request enrichment middleware
├── static/
│   ├── index.html    # Dashboard UI
│   └── style.css     # Styling
└── tools/            # 62+ tool modules
    ├── uuid/router.py
    ├── time/router.py
    └── ...
```

## Tools by Category

### Core Utilities
- `/uuid` - Generate UUID v4
- `/time` - Current time (ISO, Unix, RFC2822)
- `/password` - Secure password generator
- `/hash` - SHA256/MD5 hashing
- `/base64` - Encode/decode strings
- `/slug` - URL-friendly string conversion
- `/color` - Hex/RGB conversion

### Developer Tools (Batch 8)
- `/timestamp` - Unix timestamp conversion
- `/cron` - Cron expression parser
- `/jwt` - JWT token decoder
- `/url` - URL encoder/decoder/parser
- `/markdown` - Markdown to HTML

### Content & Fun
- `/lorem` - Lorem Ipsum generator
- `/dadjoke` - Random dad jokes
- `/zen` - Zen of Python
- `/quote` - Tech quotes
- `/shrug` - ¯\_(ツ)_/¯
- `/flip` - Table flip text
- `/decision` - Coin flip, 8-ball

### Fun & Social (Batch 9)
- `/emoji` - Random emoji generator
- `/ascii` - Text to ASCII art
- `/fortune` - Fortune cookie messages
- `/commit` - Random commit messages
- `/roast` - Developer roasts 🔥
- `/compliment` - Developer compliments ✨

### Inspection & Lookup
- `/ip` - Client IP address
- `/headers` - Request headers
- `/http` - HTTP status codes
- `/country` - Country code lookup
- `/mime` - MIME type lookup
- `/port` - Port number lookup

### Data & Text
- `/case` - Text case conversion
- `/regex` - Regex tester
- `/json` - JSON formatter
- `/xml` - XML formatter
- `/csv` - JSON to CSV
- `/sort` - Sort text lines
- `/diff` - Text diff

### Logic & Ciphers
- `/diceware` - Passphrase generator
- `/luhn` - Credit card validation
- `/isbn` - ISBN validation
- `/morse` - Morse code
- `/leet` - 1337 speak
- `/rot13` - ROT13 cipher
- `/prime` - Prime checker

### Calculators
- `/unit` - Unit conversion
- `/bmi` - BMI calculator
- `/emi` - Loan EMI calculator
- `/percent` - Percentage calculations
- `/palette` - Color palette generator

### Visuals
- `/qr` - QR code generator
- `/placeholder` - Placeholder images
- `/badge` - SVG status badges

## Adding a New Tool

1. Create folder: `app/tools/newtool/`
2. Create router: `app/tools/newtool/router.py`

```python
from fastapi import APIRouter
from app.core.response import APIResponse

router = APIRouter()

@router.get("")
async def my_tool():
    return APIResponse.success(
        message="Tool response",
        data={"result": "value"}
    )
```

3. Register in `main.py`:
```python
from app.tools.newtool import router as newtool_router
app.include_router(newtool_router.router, prefix="/newtool", tags=["Newtool"])
```

4. Add to tags_metadata in `main.py`

## Response Format

All endpoints return a consistent JSON structure:

```json
{
  "success": true,
  "message": "Description",
  "data": { ... }
}
```

Error responses:
```json
{
  "success": false,
  "error": "Error message"
}
```

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Deployment

- **Heroku**: Uses `Procfile`
- **Vercel**: Uses `vercel.json`
- **Docker**: Uses `Dockerfile`

## Rate Limiting

Default: 120 requests/minute per IP (via slowapi)

## Key Files

| File | Purpose |
|------|---------|
| `main.py` | App initialization, all router imports |
| `core/response.py` | `APIResponse.success()` and `.error()` |
| `static/index.html` | Dashboard with search, themes, try-it |
| `requirements.txt` | Dependencies: fastapi, uvicorn, slowapi |

## Design Philosophy

- **Stateless**: No database, no session state
- **Independent**: Each tool works in isolation
- **Lightweight**: Minimal dependencies
- **Fast**: No heavy processing, instant responses
