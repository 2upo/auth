from fastapi import APIRouter, Depends

from . import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import service


router = APIRouter()


@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(service.require_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user

