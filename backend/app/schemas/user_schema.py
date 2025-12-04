from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str
    gudang_id: Optional[int] = None

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    gudang_id: Optional[int]

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    role: str
