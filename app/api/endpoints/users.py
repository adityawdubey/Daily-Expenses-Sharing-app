#User Management Endpoints

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import models
from app.api.schemas import user as user_schema
from app.core.database import get_db

router = APIRouter()

@router.post("/users/")
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email, mobile=user.mobile)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
