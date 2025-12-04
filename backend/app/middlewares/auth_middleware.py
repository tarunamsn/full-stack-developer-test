from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.jwt import decode_access_token
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        path = request.url.path

        # Skip public endpoints
        public_paths = [
            "/api/v1/auth/login",
            "/api/v1/auth/generate-token",
            "/docs",
            "/openapi.json",
            "/openapi",
        ]

        if path in public_paths:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid authorization token"
            )

        token = auth_header.split(" ")[1]

        try:
            payload = decode_access_token(token)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        user_id = int(payload["sub"])
        role = payload["role"]

        db: Session = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        db.close()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        request.state.user = user

        return await call_next(request)

