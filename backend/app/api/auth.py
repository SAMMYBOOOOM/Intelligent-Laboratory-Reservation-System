from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    # Check user credentials
    if not user or user.password != data.password:
        return {"code": 400, "message": "User not found or password incorrect"}
    return {
        "code": 200,
        "message": "User login successful",
        "data": UserResponse.model_validate(user),
    }
