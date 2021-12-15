"""
Common utilities for database operations
"""
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from database.config_db import Base, SessionLocal
from database import models

"""
Select columns to sort based on query parameters
"""
columns = {
    "id":models.User.id,
    "first_name":models.User.first_name,
    "last_name":models.User.last_name,
    "company_name":models.User.company_name,
    "city": models.User.city,
    "state":models.User.state,
    "zip":models.User.zip,
    "email":models.User.email,
    "web":models.User.web,
    "age":models.User.age,
    "-id":models.User.id.desc(),
    "-first_name":models.User.first_name.desc(),
    "-last_name":models.User.last_name.desc(),
    "-company_name":models.User.company_name.desc(),
    "-city": models.User.city.desc(),
    "-state":models.User.state.desc(),
    "-zip":models.User.zip.desc(),
    "-email":models.User.email.desc(),
    "-web":models.User.web.desc(),
    "-age":models.User.age.desc()
}

def get_db():
    """
    Get database session
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
    
def commit_changes_to_object(database: Session, obj: Base):
    """
    Finish the database transaction and refresh session
    """
    database.add(obj)
    database.commit()
    database.refresh(obj)