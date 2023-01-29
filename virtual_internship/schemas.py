from pydantic import BaseModel
from datetime import datetime


class PerevalBase(BaseModel):
    beauty_title: str
    title: str
    other_title: str
    connect: str
    add_time: datetime

    class Config:
        orm_mode = True


class PerevalList(PerevalBase):
    id: int


class PerevalCreate(PerevalBase):
    pass


