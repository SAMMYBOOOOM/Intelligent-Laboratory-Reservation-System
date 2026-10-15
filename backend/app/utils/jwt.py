from datetime import datetime, timedelta
import jwt
from app.config import settings

def create_access_token(user_id: int) -> str:
    """Create JWT token"""
    expire = datetime.now() + timedelta(hours=settings.JWT_EXPIRE_HOURS)

    payload = {"user_id": user_id, "exp": expire}  # exp is fixed key, cannot be changed

    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

def decode_access_token(token: str) -> dict:
    """Decode jwt token"""
    # print(token)
    return jwt.decode(
        token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )