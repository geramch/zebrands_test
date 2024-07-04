from fastapi import APIRouter
from app.routers.products.endpoints import router as products
from app.routers.auth.endpoints import router as auth
from app.routers.initial_admin.endpoints import router as initial_admin
from app.routers.users.endpoints import router as users

api_v1_router = APIRouter()
api_v1_router.include_router(products)
api_v1_router.include_router(auth)
api_v1_router.include_router(initial_admin)
api_v1_router.include_router(users)
