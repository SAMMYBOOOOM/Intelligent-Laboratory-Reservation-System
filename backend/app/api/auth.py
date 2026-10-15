from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Search database by username
    user = db.query(User).filter(User.username == data.username).first()

    # Check user credentials
    if not user or not verify_password(data.password, user.password):
        return {"code": 400, "message": "Username or password is incorrect"}
    # Check user status
    if user.status != 1:
        return {"code": 403, "message": "User is disabled"}
    # Create token
    token = create_access_token(user.id)
    # Return response
    return {
        "code": 200,
        "message": "Login successful",
        "data": {"token": token, "user": UserResponse.model_validate(user)},
    }