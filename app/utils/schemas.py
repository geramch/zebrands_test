from pydantic import BaseModel

class ProductBase(BaseModel):
    sku: str
    name: str
    price: float
    brand: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str
    price: float
    brand: str

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
