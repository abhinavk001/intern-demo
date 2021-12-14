"""
Database Models
"""
from sqlalchemy import Column, String, Integer
from database.config_db import Base


class User(Base):
    """
    USER MODEL
    userID, first_name, last_name, company_name, city, state, zip, email, web, age
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    company_name = Column(String(50), nullable=False)
    city = Column(String(50))
    state = Column(String(50))
    zip = Column(Integer, nullable=False)
    email = Column(String(255),nullable=False, unique=True)
    web = Column(String(255))
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.first_name
