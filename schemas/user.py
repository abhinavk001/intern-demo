"""
User schemas
"""
from typing import Optional
from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    """
    Create user model
    """
    id: int
    first_name: str
    last_name: str
    company_name: str
    city: str
    state: str
    zip: int
    email: EmailStr
    web: str
    age: int

class UpdateUser(BaseModel):
    """
    Update user model
    """
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]