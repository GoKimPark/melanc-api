from pydantic import BaseModel, Field, validator
from datetime import datetime

from melanc.utils.enums import Weather, Feeling


class DiaryBase(BaseModel):
    user_id: int
    title: str = Field(max_length=100)
    weather: str
    feeling: str
    content: str

    @validator("weather")
    def validate_weather(cls, value):
        assert value in [weather.value for weather in Weather]

    @validator("feeling")
    def validate_feeling(cls, value):
        assert value in [feeling.value for feeling in Feeling]


class DiaryCreate(DiaryBase):
    pass


class Diary(DiaryBase):
    id: int
    deleted: datetime = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
