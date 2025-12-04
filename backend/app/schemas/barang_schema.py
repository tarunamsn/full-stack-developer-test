from pydantic import BaseModel, validator

class BarangBase(BaseModel):
    name: str
    kategori: str
    stok: int
    harga_beli: float
    harga_jual: float
    min_stok: int

    @validator("stok")
    def stock_cannot_be_negative(cls, v):
        if v < 0:
            raise ValueError("STOK TIDAK BISA MINUS!")
        return v

    @validator("harga_jual")
    def selling_price_greater_than_purchase(cls, v, values):
        if "harga_jual" in values and v <= values["harga_beli"]:
            raise ValueError("HARGA JUAL HARUS LEBIH TINGGI DARI HARGA BELI!")
        return v


class BarangCreate(BarangBase):
    pass


class BarangUpdate(BarangBase):
    pass


class BarangOut(BaseModel):
    id: int
    name: str
    kategori: str
    stok: int
    harga_beli: float
    harga_jual: float
    min_stok: int
    gudang_id: int

    class Config:
        orm_mode = True
