from typing import Any
from pydantic import BaseModel

class Response(BaseModel):
    """Unified encapsulated response format"""

    code: int
    message: str
    data: Any = None

    @classmethod
    def success(cls, message: str = "Request successful", data: Any = None):
        return cls(code=200, message=message, data=data)

    @classmethod
    def error(cls, code: int = 500, message: str = "Request failed"):
        return cls(code=code, message=message)