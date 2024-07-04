import app.db.utils as db_utils

from fastapi import FastAPI
from app.routers.routers import api_v1_router as routers

db_utils.init_db()

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(routers)