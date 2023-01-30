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
    user: List[BaseUser]
    #user_id: int

    class Config:
        orm_mode = True


class PerevalList(PerevalBase):
    id: int


class PerevalCreate(PerevalBase):
    pass


class PerevalUpdate(PerevalBase):
    pass


