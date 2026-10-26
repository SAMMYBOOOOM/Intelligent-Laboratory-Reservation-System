from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError

from app.models.user import User
from app.database import Base, engine
from app.api import api
from app.common.exceptions import (
    BusinessException,
    bussiness_excpetion_hadler,
    http_excpetion_hadler,
    validation_excpetion_hadler,
    global_excpetion_hadler,
)

Base.metadata.create_all(bind=engine)   # Create database tables

app = FastAPI()
app.include_router(api)

# Register exception handlers
app.add_exception_handler(BusinessException, bussiness_excpetion_hadler)
app.add_exception_handler(HTTPException, http_excpetion_hadler)
app.add_exception_handler(RequestValidationError, validation_excpetion_hadler)
# Global exception handler
app.add_exception_handler(Exception, global_excpetion_hadler)

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}