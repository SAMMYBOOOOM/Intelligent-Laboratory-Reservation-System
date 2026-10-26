from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.common.response import Response

class BusinessException(Exception):
    """Custom business exception"""

    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(message)

async def bussiness_excpetion_hadler(request: Request, exc: BusinessException):
    """Custom business exception handler"""
    return JSONResponse(
        status_code=200,
        content=Response.error(code=exc.code, message=exc.message).model_dump(),
    )

async def http_excpetion_hadler(request: Request, exc: HTTPException):
    """HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content=Response.error(code=exc.status_code, message=exc.detail).model_dump(),
    )

async def validation_excpetion_hadler(request: Request, exc: RequestValidationError):
    """Parameter exception handler"""
    return JSONResponse(
        status_code=422,
        content=Response.error(code=422, message="Request parameter validation error").model_dump(),
    )

async def global_excpetion_hadler(request: Request, exc: Exception):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content=Response.error(code=500, message="Internal server error").model_dump(),
    )