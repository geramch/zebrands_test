from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.schemas import UserFirstAdmin, User, UserCreate
from app.services.users_service import user_service
from app.db.utils import get_db

router = APIRouter(
    prefix="/initial_admin",
    tags=["Initial Admin"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=User)
def create_initial_admin(user: UserFirstAdmin, db: Session = Depends(get_db)):
    admin_count = user_service.get_admin_count(db)
    if admin_count > 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins already exist. Initial admin creation is not allowed.",
        )
    create_user_obj = UserCreate(
        username=user.username,
        password=user.password,
        is_admin=True
    )
    return user_service.create_user(db=db, user=create_user_obj)
