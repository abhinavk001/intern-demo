"""
Entrypoint
"""
from logging import error
from fastapi import FastAPI, Depends
from typing import Optional
from sqlalchemy import or_
from sqlalchemy.sql.functions import user
from sqlalchemy.orm import Session
from fastapi_pagination import Page, Params, paginate
from database.database import set_up_database
from database import models
from utils import get_db, columns


app = FastAPI()

models.Base.metadata.create_all(set_up_database())

@app.get("/")
def home():
    """
    Homepage
    """
    return {"greetings":"hello"}

@app.get("/api/users", )
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