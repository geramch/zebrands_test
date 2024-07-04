from fastapi import FastAPI
from app.routers.routers import api_v1_router as routers
from sqlalchemy.orm import Session
from app.services.users_service import user_service
from app.db.utils import get_db

import app.db.utils as db_utils

db_utils.init_db()

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(routers)

@app.on_event("startup")
async def startup_event():
    db: Session = next(get_db())
    admin_count = user_service.get_admin_count(db)
    if admin_count == 0:
        print("No admins found. You can create an initial admin using the /initial_admin endpoint.")
