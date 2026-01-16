"""
Cloudflare Workers entry point for Bude Utils API
"""
from workers import WorkerEntrypoint
import asgi

# Import the main FastAPI app from the existing structure
import sys
import os

# Add the parent directory to the path so we can import from app/
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.main import app


class Default(WorkerEntrypoint):
    """
    Cloudflare Workers entrypoint class.
    This wraps our existing FastAPI application for Workers deployment.
    """
    
    async def fetch(self, request):
        """
        Handle incoming requests and pass them to the FastAPI app
        """
        return await asgi.fetch(app, request, self.env)
