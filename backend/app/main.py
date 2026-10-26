from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError

from app.models.user import User
from app.database import Base, engine
from app.api import api
from starlette.middleware.cors import CORSMiddleware
from app.common.exceptions import (
    BusinessException,
    bussiness_excpetion_hadler,
    http_excpetion_hadler,
    validation_excpetion_hadler,
    global_excpetion_hadler,
)

Base.metadata.create_all(bind=engine)   # Create database tables

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allowed frontend origins; do not simply write ["*"]
    allow_credentials=True,       # ✅ Key: allow the frontend to carry the Authorization token
    allow_methods=["*"],          # Allow all request methods: GET POST PUT DELETE OPTIONS
    allow_headers=["*"],          # Allow all request headers (including Authorization)
)

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