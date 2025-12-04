from sqlalchemy.orm import Session
from app.models.gudang import Gudang

class GudangRepository:

    @staticmethod
    def get(db: Session, gudang_id: int):
        return db.query(Gudang).filter(Gudang.id == gudang_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Gudang).all()
