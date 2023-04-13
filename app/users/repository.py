from app.users.models import User
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends


def get_by_id(user_id: str, db: Session = Depends(get_db)):
    return db.query(User).get(user_id)

def get_by_email(user_email: str, db: Session = Depends(get_db)):
    return db.query(User).filter(
        User.email == user_email).first()

def create_user(new_user: dict, db: Session = Depends(get_db)):
    user = User(**new_user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.to_dict()