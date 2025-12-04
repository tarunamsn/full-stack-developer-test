from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.barang import Barang
from app.schemas.barang_schema import BarangCreate, BarangUpdate
from app.repositories.barang_repository import BarangRepository

class BarangService:

    @staticmethod
    def create_barang(db: Session, data: BarangCreate, gudang_id: int):
        return BarangRepository.create(db, data, gudang_id)

    @staticmethod
    def get_barang_by_role(db: Session, role: str, gudang_id: int):
        if role == "super_admin":
            return BarangRepository.get_all(db)
        return BarangRepository.get_all_by_gudang(db, gudang_id)

    @staticmethod
    def update_barang(db: Session, barang: Barang, data: BarangUpdate):
        if data.stok < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="STOK TIDAK BISA MINUS!"
            )

        return BarangRepository.update(db, barang, data)

    @staticmethod
    def delete_barang(db: Session, barang: Barang):
        if barang.stok > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="STOK HARUS KOSONG SEBELUM BISA DIHAPUS!"
            )

        return BarangRepository.delete(db, barang)
