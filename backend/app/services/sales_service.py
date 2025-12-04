from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.sales_repository import SalesRepository
from app.repositories.barang_repository import BarangRepository
from app.schemas.sale_schema import SaleCreate

class SalesService:

    @staticmethod
    def get_all_sales(db: Session):
        return SalesRepository.get_all(db)

    @staticmethod
    def create_sale(db: Session, data: SaleCreate):
        barang = BarangRepository.get(db, data.barang_id)

        if not barang:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="BARANG TIDAK ADA!"
            )

        if barang.stok < data.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="KETERSEDIAAN BARANG MENIPIS!"
            )

        # Update stock
        barang.stok -= data.quantity
        db.commit()
        db.refresh(barang)

        # Log sale
        return SalesRepository.create(db, data)
