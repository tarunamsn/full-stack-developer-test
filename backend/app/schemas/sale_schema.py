from pydantic import BaseModel, validator

class SaleCreate(BaseModel):
    barang_id: int
    quantity: int

    @validator("quantity")
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError("JUMLAH BARANG TIDAK BISA MINUS!")
        return v


class SaleOut(BaseModel):
    id: int
    barang_id: int
    quantity: int

    class Config:
        orm_mode = True
