from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    sku: str
    name: str
    price: float
    brand: str
    query_count: Optional[int] = 0  # Inicializado a 0 por defecto

    class Config:
        orm_mode = True

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

class UserFirstAdmin(BaseModel):
    username: str
    password: str
    email: str
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    username: str
    password: str
    email: str
    is_admin: bool

class UserUpdate(UserBase):
    password: str
    is_admin: bool

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None