from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from melanc.core.base import BaseDBModel
from melanc.utils.enums import Gender


class User(BaseDBModel):
    __tablename__ = "users"

    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    gender = Column(Gender)
    age = Column(Integer, nullable=False)
    last_login = Column(DateTime, default=datetime.now())

    diaries = relationship("Diary", back_populates="user")
