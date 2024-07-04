import pytz

from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine, ForeignKey, Float,
    Boolean
)

from app.db.utils import Base

TIME_ZONE = pytz.timezone("America/Mexico_City")

class Products(Base):
    __tablename__ = 'products'

    sku = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    brand = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)