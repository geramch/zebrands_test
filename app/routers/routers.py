from fastapi import APIRouter
from app.routers.products.endpoints import router as products

api_v1_router = APIRouter()
api_v1_router.include_router(products)
