# services/users/project/api/users.py

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy import exc
from sqlalchemy.orm import Session

from project.api.models import User
from project.api.schemas import UserCreate
from project.config import BaseConfig, get_settings
from project.db import get_db

router = APIRouter()


@router.get("/users/ping")
def users_ping(settings: BaseConfig = Depends(get_settings)):
    return {
        "status": "success",
        "message": "pong!",
        "environment": settings.ENVIRONMENT,
        "testing": settings.TESTING,
    }


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    user = db.query(User).filter(User.email == payload.email).first()
    if user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"status": "fail", "message": "Sorry. That email already exists."},
        )
    try:
        user = User(username=payload.username, email=payload.email)
        db.add(user)
        db.commit()
        return {"status": "success", "message": f"{payload.email} was added!"}
    except exc.IntegrityError:
        db.rollback()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"status": "fail", "message": "Invalid payload."},
        )


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"status": "fail", "message": "User does not exist"},
        )
    return {
        "status": "success",
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "active": user.active,
        },
    }

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {
        "status": "success",
        "data": {
            "users": [user.to_json() for user in users]
        }
    }
