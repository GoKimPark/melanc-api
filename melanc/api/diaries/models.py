from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from melanc.core.base import BaseDBModel
from melanc.utils.enums import Weather, Feeling


class Diary(BaseDBModel):
    __tablename__ = "diaries"

    user = relationship("User", back_populates="diaries")
    title = Column(String(length=100))
    weather = Column(Weather, nullable=False)
    feeling = Column(Feeling, nullable=False)
    content = Column(String, nullable=False)
