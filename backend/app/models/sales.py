from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    barang_id = Column(Integer, ForeignKey("barang.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    barang = relationship("Barang", back_populates="sales")
