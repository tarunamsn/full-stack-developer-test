from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.jwt import decode_access_token

class AuthMidDummy(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # Skip login endpoint & docs
        if "login" in request.url.path or request.url.path.startswith("/docs") or request.url.path.startswith("/openapi") or "generate-token" in request.url.path:
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

        request.state.user = {
            "id": int(payload["sub"]),
            "role": payload["role"]
        }

        return await call_next(request)
