from fastapi import HTTPException, status, Request

class RoleChecker:

    @staticmethod
    def super_admin_only(request: Request):
        if request.state.user.role != "super_admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="YANG BISA AKSES INI HANYALAH ADMIN!"
            )

    @staticmethod
    def gudang_only(request: Request):
        if request.state.user.role != "gudang":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="YANG BISA AKSES INI HANYALAH PEMILIK GUDANG!"
            )

    @staticmethod
    def ensure_not_super_admin_for_write(request: Request):
        """
        ADMIN CUMA BISA READ-ONLY.
        """
        if request.state.user.role == "super_admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="ADMIN HANYA BERSIFAT READ-ONLY!"
            )

    @staticmethod
    def barang_gudang_permission(request: Request, barang):
        """
        PEMILIK GUDANG DAPAT MELAKUKAN CRUD.
        ADMIN TIDAK DIPERBOLEHKAN MELAKUKAN CRUD.
        """
        user = request.state.user

        # Prevent super admin from modifying
        if user.role == "super_admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="ADMIN HANYA BERSIFAT READ-ONLY!"
            )

        # Warehouse users must only modify items in their warehouse
        if barang.gudang_id != user.gudang_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="ANDA TIDAK DIPERBOLEHKAN MELAKUKAN PERUBAHAN PADA ITEM BARANG INI!"
            )
