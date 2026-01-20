"""
Vercel serverless function entry point for Bude Utils API
"""
import sys
from pathlib import Path

# Add the src directory to the path so we can import the app
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

try:
    # Import the FastAPI app
    from app.main import app
    
    # This is the handler that Vercel will call
    # Vercel's Python runtime expects the app to be exposed directly
    handler = app
    print("Successfully imported app", file=sys.stderr)
except Exception as e:
    print(f"Failed to import app: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    raise e
