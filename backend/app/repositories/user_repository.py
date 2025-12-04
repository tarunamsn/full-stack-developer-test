from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

class UserRepository:

    @staticmethod
    def get_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db: Session, user: UserCreate):
        hashed_pwd = hash_password(user.password)
        db_user = User(
            username=user.username,
            password=hashed_pwd,
            role=user.role,
            gudang_id=user.gudang_id,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
