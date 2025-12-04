from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user_schema import UserCreate
from app.repositories.user_repository import UserRepository
from app.repositories.gudang_repository import GudangRepository

class UserService:

    @staticmethod
    def create_user(db: Session, data: UserCreate):
        if UserRepository.get_by_username(db, data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="USERNAME SUDAH ADA!"
            )

        if data.role == "gudang":
            gudang = GudangRepository.get(db, data.gudang_id)
            if not gudang:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="GUDANG YANG DIMAKSUD TIDAK ADA!"
                )

        return UserRepository.create(db, data)
