from sqlalchemy.orm import Session
from app.models.barang import Barang
from app.schemas.barang_schema import BarangCreate, BarangUpdate

class BarangRepository:

    @staticmethod
    def get_all_by_gudang(db: Session, gudang_id: int):
        return (
            db.query(Barang)
            .filter(Barang.gudang_id == gudang_id)
            .order_by(Barang.id.desc())
            .all()
        )

    @staticmethod
    def get_all(db: Session):
        return db.query(Barang).order_by(Barang.id.desc()).all()

    @staticmethod
    def get(db: Session, barang_id: int):
        return db.query(Barang).filter(Barang.id == barang_id).first()

    @staticmethod
    def create(db: Session, data: BarangCreate, gudang_id: int):
        barang = Barang(**data.dict(), gudang_id=gudang_id)
        db.add(barang)
        db.commit()
        db.refresh(barang)
        return barang

    @staticmethod
    def update(db: Session, barang: Barang, data: BarangUpdate):
        for field, value in data.dict().items():
            setattr(barang, field, value)
        db.commit()
        db.refresh(barang)
        return barang

    @staticmethod
    def delete(db: Session, barang: Barang):
        db.delete(barang)
        db.commit()
