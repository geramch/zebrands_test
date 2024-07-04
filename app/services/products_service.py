from sqlalchemy.orm import Session
from app.db.db import Products
from app.utils.schemas import *

class CRUDProducts:
    # Retrieve a single product by its ID
    def get_product(self, db: Session, product_id: int):
        return db.query(Products).filter(Products.id == product_id).first()

    # Retrieve a list of products with pagination
    def get_products(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Products).offset(skip).limit(limit).all()

    # Create a new product
    def create_product(self, db: Session, product: ProductCreate):
        db_product = Products(sku=product.sku, name=product.name, price=product.price, brand=product.brand)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    # Update an existing product by its ID
    def update_product(self, db: Session, product_id: int, product: ProductUpdate):
        db_product = db.query(Products).filter(Products.id == product_id).first()
        if db_product is None:
            return None
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

    # Delete a product by its ID
    def delete_product(self, db: Session, product_id: int):
        db_product = db.query(Products).filter(Products.id == product_id).first()
        if db_product is None:
            return None
        db.delete(db_product)
        db.commit()
        return db_product

# Instance of CRUDProducts to be used in the routes
product_service = CRUDProducts()
