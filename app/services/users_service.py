from sqlalchemy.orm import Session
from app.db.db import User
from app.utils.schemas import UserCreate, UserUpdate

class CRUDUser:
    def create_user(self, db: Session, user: UserCreate):
        from app.auth.auth import get_password_hash
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password, is_admin=user.is_admin, is_active=True)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user(self, db: Session, user_id: int, user: UserUpdate):
        from app.auth.auth import get_password_hash
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            if user.password:
                db_user.hashed_password = get_password_hash(user.password)
            db_user.is_admin = user.is_admin
            db.commit()
            db.refresh(db_user)
        return db_user

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def get_admin_count(self, db: Session):
        return db.query(User).filter(User.is_admin == True).count()


user_service = CRUDUser()
