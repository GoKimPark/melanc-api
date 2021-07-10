import re
from datetime import datetime
from pydantic import BaseModel, validator

from melanc.apps.users.models import Gender


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    gender: Gender
    age: int

    @validator("age")
    def validate_age(cls, age):
        assert age >= 0, "age cannot be a negative number."
        return age

    @validator("email")
    def validate_email(cls, email):
        email_pattern = re.compile("^[a-zA-Z0-9]+@[a-z]+.[a-z]+$")
        if not email_pattern:
            raise ValueError("invalid email format")

        return email

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime = None
    deleted: datetime = None
