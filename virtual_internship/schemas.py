from pydantic import BaseModel
from datetime import datetime
from user.schemas import BaseUser
from typing import List


class PerevalBase(BaseModel):
    beauty_title: str
    title: str
    other_title: str
    connect: str
    add_time: datetime
    user: int
    coords: int
    level: int
    pereval_area: int
    #user_id: int

    class Config:
        orm_mode = True


class PerevalList(PerevalBase):
    id: int


class PerevalCreate(PerevalBase):
    pass


class PerevalUpdate(BaseModel):
    beauty_title: str
    title: str
    other_title: str
    connect: str
    add_time: datetime
    coords: int
    level: int
    pereval_area: int


