from fastapi import APIRouter, Depends
from app.models.user import User
from app.dependencies.auth import get_current_user
from app.schemas.user import UserResponse

router = APIRouter(prefix="/user", tags=["User info window"])

@router.get("/info")
def get_user_info(current_user: User = Depends(get_current_user)):
    """Retrieve current user information"""
    return {
        "code": 200,
        "message": "Request successfully",
        "data": UserResponse.model_validate(current_user),
}