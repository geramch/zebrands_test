from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.services.products_service import product_service
from app.utils.schemas import *
from app.db.utils import get_db
from app.auth.auth import get_current_active_admin, get_current_active_user

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)

# Create a new product (Admin only)
@router.post("/", response_model=ProductBase)
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_admin)):
    return product_service.create_product(db=db, product=product)

# Read a list of products (Accessible by all users)
@router.get("/", response_model=List[ProductBase])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return product_service.get_products(db=db, skip=skip, limit=limit)

# Read a single product by its ID (Accessible by all users)
@router.get("/{product_id}", response_model=ProductBase)
def read_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_product = product_service.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Update an existing product by its ID (Admin only)
@router.put("/{product_id}", response_model=ProductBase)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_admin)):
    db_product = product_service.update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Delete a product by its ID (Admin only)
@router.delete("/{product_id}", response_model=ProductBase)
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_admin)):
    db_product = product_service.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
