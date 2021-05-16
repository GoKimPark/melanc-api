from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

from melanc.core.db import Base


class BaseDBModel(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    deleted = Column(DateTime, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
