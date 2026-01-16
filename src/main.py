"""
Cloudflare Workers entry point for Bude Utils API
"""
from workers import WorkerEntrypoint
import asgi

# Import the main FastAPI app
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
