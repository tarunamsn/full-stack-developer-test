from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user_schema import UserCreate, UserOut
from app.services.user_service import UserService
from app.middlewares.role_checker import RoleChecker

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(
    request: Request,
    data: UserCreate,
    db: Session = Depends(get_db)
):
    # Writing = super admin not allowed?
    # If you want super admin to create users, comment this line below,
    # And uncomment this line again to prevent super admin for doing so:
    RoleChecker.ensure_not_super_admin_for_write(request)

    return UserService.create_user(db, data)
