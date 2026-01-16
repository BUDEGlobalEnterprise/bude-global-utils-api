from typing import Any, Optional
from fastapi.responses import JSONResponse

class APIResponse:
    @staticmethod
    def success(data: Any, message: str = "success") -> dict:
        """Standard success response wrapper"""
        return {
            "status": "success",
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message: str, code: int = 400, details: Optional[Any] = None) -> JSONResponse:
        """Standard error response wrapper"""
        content = {
            "status": "error",
            "message": message
        }
        if details:
            content["details"] = details
            
        return JSONResponse(
            status_code=code,
            content=content
        )
