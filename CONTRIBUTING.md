# Contributing to Bude Utils API

We keep this consistent and simple. Here are the rules:

## Core Rules

1. **No Databases**: If it needs state persistence, it doesn't belong here.
2. **No Authentication**: Tools should be public and require no login.
3. **No Cross-dependencies**: One tool should not depend on another tool's logic.
4. **Keep it Small**: Endpoints should do one thing well.

## How to add a tool

1. Create a new folder in `app/tools/<tool_name>`.
2. Create a `router.py` file.
3. If you need static data, put it in `data.json` inside your tool folder.
4. Register your router in `app/main.py`.

## Commit Messages

Keep them clear and descriptive.
Example: `feat: add coin flip decision tool`
