from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func

from melanc.core.db import Base
from melanc.utils.enums import Gender


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    deleted = Column(DateTime, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    gender = Column(Enum(Gender))
    age = Column(Integer, nullable=False)
    last_login = Column(DateTime, default=datetime.now())

    # diaries = relationship("Diary", back_populates="user")
