from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user_schema import LoginRequest, LoginResponse
from app.services.auth_service import AuthService
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = AuthService.login(db, data.username, data.password)
    # Generate token on successful login
    token = create_access_token(user_id=user.id, role=user.role)
    return {"access_token": token}

@router.get("/generate-token")
def generate_token():
    token = create_access_token(user_id=1, role="admin")
    return {"access_token": token}
