from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.barang_schema import BarangCreate, BarangUpdate, BarangOut
from app.services.barang_service import BarangService
from app.middlewares.role_checker import RoleChecker
from app.repositories.barang_repository import BarangRepository

router = APIRouter(prefix="/items", tags=["Items"])

# ----------------------------------------------------------------------
# READ (ALLOWED FOR BOTH warehouse & super_admin)
# ----------------------------------------------------------------------

@router.get("/", response_model=list[BarangOut])
def get_items(request: Request, db: Session = Depends(get_db)):
    user = request.state.user
    return BarangService.get_barang_by_role(db, user.role, user.gudang_id)

# ----------------------------------------------------------------------
# CREATE (super_admin cannot modify)
# ----------------------------------------------------------------------

@router.post("/", response_model=BarangOut)
def create_item(
    request: Request,
    data: BarangCreate,
    db: Session = Depends(get_db)
):
    # Block super_admin from modifying
    RoleChecker.ensure_not_super_admin_for_write(request)
    user = request.state.user

    return BarangService.create_barang(db, data, user.gudang_id)

# ----------------------------------------------------------------------
# UPDATE (super_admin cannot modify)
# ----------------------------------------------------------------------

@router.put("/{barang_id}", response_model=BarangOut)
def update_item(
    barang_id: int,
    data: BarangUpdate,
    request: Request,
    db: Session = Depends(get_db)
):
    # Block super_admin from MODIFYING
    RoleChecker.ensure_not_super_admin_for_write(request)

    barang = BarangRepository.get(db, barang_id)
    if not barang:
        raise HTTPException(status_code=404, detail="BARANG TIDAK ADA")

    # Warehouse user can only modify own warehouse items
    RoleChecker.barang_gudang_permission(request, barang)

    return BarangService.update_barang(db, barang, data)

# ----------------------------------------------------------------------
# DELETE (super_admin cannot modify)
# ----------------------------------------------------------------------

@router.delete("/{barang_id}")
def delete_barang(barang_id: int, request: Request, db: Session = Depends(get_db)):
    # Block super admin modification
    RoleChecker.ensure_not_super_admin_for_write(request)

    barang = BarangRepository.get(db, barang_id)
    if not barang:
        raise HTTPException(status_code=404, detail="BARANG TIDAK ADA")

    RoleChecker.barang_gudang_permission(request, barang)

    BarangService.delete_barang(db, barang)
    return {"detail": "BARANG BERHASIL DIHAPUS!"}
