import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from melanc.core.db import Base


class Gender(enum.Enum):
    FEMALE = "female"
    MALE = "male"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    deleted = Column(DateTime, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=True, unique=True)
    gender = Column(Enum(Gender))
    age = Column(Integer)
    last_login = Column(DateTime, default=datetime.now())

    diaries = relationship("Diary", back_populates="user")
