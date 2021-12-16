"""
Entrypoint
"""
from fastapi import FastAPI, Depends, status, HTTPException
from typing import Optional
from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.database import set_up_database
from database import models
from utils import get_db, columns, commit_changes_to_object
from schemas.user import CreateUser, UpdateUser


app = FastAPI()

models.Base.metadata.create_all(set_up_database())

@app.get("/")
def home():
    """
    Homepage
    """
    return {"greetings":"hello"}

@app.get("/api/users")
def get_users(page: int = 1, limit: int = 5, name:Optional[str] = None, sort:Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get information about all users
    """
    users = db.query(models.User)
    if name:
        users = db.query(models.User).filter(or_(models.User.first_name.ilike('%'+name+'%'), models.User.last_name.ilike('%'+name+'%')))
    if sort:
        users = users.order_by(columns[sort])


    users = users.limit(limit).offset(limit*(page-1)).all()

    return users

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def create_user(request:CreateUser, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    new_request = models.User(**request.dict())
    try:
        commit_changes_to_object(db, new_request)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User already exists")
    return {"message":"User created successfully"}

@app.get("/api/users/{id}", status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    """
    Get information about all users
    """
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    return user
    
@app.patch("/api/users/{id}", status_code=status.HTTP_200_OK)
def update_user(id: int, request:UpdateUser, db: Session = Depends(get_db)):
    """
    Update user information
    """
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    for key, value in request.dict().items():
        if value:
            setattr(user, key, value)

    commit_changes_to_object(db, user)
    return {"message":"User updated successfully"}

@app.delete("/api/users/{id}", status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session = Depends(get_db)):
    """
    Delete user based on id passed as parameter
    """
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    db.delete(user)
    db.commit()

    return {"message":"User deleted successfully"}