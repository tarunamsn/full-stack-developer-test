from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.sale_schema import SaleCreate, SaleOut
from app.services.sales_service import SalesService
from app.middlewares.role_checker import RoleChecker
from app.repositories.barang_repository import BarangRepository

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SaleOut)
def create_sale(
    request: Request,
    data: SaleCreate,
    db: Session = Depends(get_db)
):
    # Writing operation → super_admin NOT allowed
    RoleChecker.ensure_not_super_admin_for_write(request)

    # Fetch item for permission check
    barang = BarangRepository.get(db, data.barang_id)
    if not barang:
        raise HTTPException(status_code=404, detail="BARANG TIDAK ADA!")

    RoleChecker.barang_gudang_permission(request, barang)

    return SalesService.create_sale(db, data)

@router.get("/", response_model=list[SaleOut])
def list_sales(
    request: Request,
    db: Session = Depends(get_db)
):
    # READ allowed for both roles
    return SalesService.get_all_sales(db)
