from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Gudang(Base):
    __tablename__ = "gudang"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    users = relationship("User", back_populates="gudang")
    barang = relationship("Barang", back_populates="gudang")

