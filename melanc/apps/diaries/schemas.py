from pydantic import BaseModel, validator
from datetime import datetime

from melanc.apps.diaries.models import Weather, Feeling


class DiaryBase(BaseModel):
    user_id: int
    title: str
    weather: Weather
    feeling: Feeling
    content: str

    @validator("title")
    def validate_title(cls, title):
        assert len(title) <= 100, "cannot exceed max length (100 chars)"
        return title

    class Config:
        orm_mode = True


class DiaryCreate(DiaryBase):
    pass


class Diary(DiaryBase):
    id: int
    created_at: datetime
    updated_at: datetime = None
    deleted: datetime = None
