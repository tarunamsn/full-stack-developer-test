from sqlalchemy.orm import Session
from app.models.sales import Sales
from app.schemas.sale_schema import SaleCreate

class SalesRepository:

    @staticmethod
    def create(db: Session, data: SaleCreate):
        sales = Sales(**data.dict())
        db.add(sales)
        db.commit()
        db.refresh(sales)
        return sales

    @staticmethod
    def get_all(db: Session):
        return db.query(Sales).all()
