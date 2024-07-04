from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.services.products_service import product_service
from app.utils.schemas import *
from app.db.utils import get_db
import pandas as pd
import io

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)

# Create a new product
@router.post("/", response_model=ProductBase)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db=db, product=product)

# Read a list of products with pagination
@router.get("/", response_model=List[ProductBase])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return product_service.get_products(db=db, skip=skip, limit=limit)

# Read a single product by its ID
@router.get("/{product_id}", response_model=ProductBase)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Update an existing product by its ID
@router.put("/{product_id}", response_model=ProductBase)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = product_service.update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Delete a product by its ID
@router.delete("/{product_id}", response_model=ProductBase)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
