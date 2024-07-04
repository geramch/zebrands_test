import os
import uuid
import pytz
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine, ForeignKey, Float,
)

from app.db.utils import Base

TIME_ZONE = pytz.timezone("America/Mexico_City")

class Products(Base):
    __tablename__ = 'products'

    sku = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    brand = Column(String)