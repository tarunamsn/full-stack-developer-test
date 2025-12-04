from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String(20), nullable=False)
    gudang_id = Column(Integer, ForeignKey("gudang.id"), nullable=True)

    gudang = relationship("Gudang", back_populates="users")
