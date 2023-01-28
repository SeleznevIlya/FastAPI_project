from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genres(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(...,max_length=25)
    last_name: str
    age: int = Field(...,)

    # @validator("age")
    # def check_age(cls, v):
    #     if v < 15 > 90:
    #         raise ValueError('error 15 more')
    #     return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genres] = []
    pages: int
