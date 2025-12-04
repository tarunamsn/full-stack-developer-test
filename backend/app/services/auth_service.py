from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.core.security import verify_password
from app.core.jwt import create_access_token

class AuthService:

    @staticmethod
    def login(db: Session, username: str, password: str):
        user = UserRepository.get_by_username(db, username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="USERNAME/PASSWORD SALAH!"
            )

        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="USERNAME/PASSWORD SALAH!"
            )

        token = create_access_token(sub=str(user.id), role=user.role)

        return {
            "token": token,
            "role": user.role
        }
