# CRUD operations for users
from sqlalchemy.orm import Session
from app.models import User

def create_user(db: Session, user_data):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, updated_data):
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in updated_data.items():
        setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

def delet_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delet(user)
        db.commit
    return user