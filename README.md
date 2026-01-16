# Bude Utils API

Small, stateless utility endpoints built and maintained by Bude Global.

## What this is

A backend-only API that provides small, reusable daily utilities (status messages, excuses, decisions, etc.) via simple HTTP endpoints.
No database. No authentication. No frontend.

## What this is not

* Not a platform
* Not a SaaS
* Not a user-tracking service

## Design Philosophy

Each endpoint is independent, stateless, and intentionally limited.
If a feature requires a database, authentication, or user state, it does not belong in this project.

## Inspiration

Inspired by [No as a Service](https://naas.isalman.dev/no).

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Adding a new utility

1. Create a folder under `app/tools/`
2. Add a `router.py`
3. Register the router in `main.py`
4. Keep it stateless and independent

## Tools List

### Core Utilities
- **UUID** (`/uuid`): Generate UUID v4.
- **Time** (`/time`): Current time in ISO, Epoch, RFC2822.
- **Base64** (`/base64`): Encode/Decode text.
- **Hash** (`/hash`): Generate SHA256/MD5 hashes.
- **Password** (`/password`): Generate secure random passwords.
- **Slug** (`/slug`): Convert string to url-friendly slug.
- **Color** (`/color`): Convert Hex <-> RGB.

### Content & Fun
- **Status** (`/status`): Random system status messages.
- **Excuse** (`/excuse`): Developer excuses.
- **Decision** (`/decision`): Coin flip, Magic 8-Ball, Choice.
- **Shrug** (`/shrug`): `¯\_(ツ)_/¯`
- **Friday** (`/friday`): Deployment safety check.
- **Synergy** (`/synergy`): Corporate buzzwords.
- **Hello** (`/hello`): Hello World in various languages.
- **Flip** (`/flip`): Table flip text `(╯°□°）╯︵ ┻━┻`.
- **Dadjoke** (`/dadjoke`): Random dad jokes.
- **Zen** (`/zen`): The Zen of Python lines.
- **Oblique** (`/oblique`): Brian Eno's strategies.
- **Quote** (`/quote`): Inspirational tech quotes.
- **Lorem** (`/lorem`): Lorem Ipsum generator.
- **Teapot** (`/brew`): RFC 2324 (418 I'm a Teapot).

### Inspection & Reference
- **IP** (`/ip`): Caller IP address.
- **Headers** (`/headers`): Reflect request headers.
- **UserAgent** (`/useragent`): Parse user agent.
- **HTTP** (`/http`): Status code descriptions.
- **Port** (`/port`): Common port lookup.
- **Mime** (`/mime`): MIME type lookup.
- **Country** (`/country`): ISO country code lookup.
- **Validate** (`/validate`): Universal validation tool.
