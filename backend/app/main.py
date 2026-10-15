from fastapi import FastAPI
from app.models.user import User
from app.database import Base, engine
from app.api.auth import router as auth_router
from app.api.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}