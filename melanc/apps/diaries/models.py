import enum

from sqlalchemy import Column, String, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from melanc.core.db import Base


class Weather(enum.Enum):
    SUNNY = "sunny"
    RAINY = "rainy"
    CLOUDY = "cloudy"
    WINDY = "windy"


class Feeling(enum.Enum):
    HAPPY = "happy"
    GOOD = "good"
    SOSO = "so_so"
    SAD = "sad"
    ANGRY = "angry"


class Diary(Base):
    __tablename__ = "diaries"

    id = Column(Integer, autoincrement=True, primary_key=True)
    deleted = Column(DateTime, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(length=100))
    weather = Column(Enum(Weather))
    feeling = Column(Enum(Feeling))
    content = Column(String)

    user = relationship("User", back_populates="diaries")
