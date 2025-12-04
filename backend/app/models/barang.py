from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Barang(Base):
    __tablename__ = "barang"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    kategori = Column(String(100), nullable=False)
    stok = Column(Integer, nullable=False, default=0)
    harga_beli = Column(Float, nullable=False)
    harga_jual = Column(Float, nullable=False)
    min_stok = Column(Integer, default=5)

    gudang_id = Column(Integer, ForeignKey("gudang.id"), nullable=False)
    gudang = relationship("Gudang", back_populates="barang")

    sales = relationship("Sale", back_populates="barang")
