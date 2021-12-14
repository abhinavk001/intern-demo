"""
Entrypoint
"""
from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from database.database import set_up_database
from database import models


app = FastAPI()

models.Base.metadata.create_all(set_up_database())

@app.get("/")
def home():
    return {"greetings":"hello"}

@app.get("/api/users")
def fun():
    return {"name":"rashid"}