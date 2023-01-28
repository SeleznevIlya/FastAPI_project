from .database import Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship


# class User(Base):
#     __tablename__ = "Perevals"
#     id = Column(Integer, primary_key=True, unique=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True, index=True)
#     phone = Column(Integer, )


class Pereval(Base):
    __tablename__ = "Perevals"

    id = Column(Integer, primary_key=True, unique=True)
    beauty_title = Column(String, unique=True)
    title = Column(String)
    other_title = Column(String)
    connect = Column(String)
    add_time = Column(DateTime)
#     coodrs = relationship("Coords")
#     level = Column()
#     image = Column()
#
#
# class PerevalImage(Base):
#     __tablename__ = "Perevals"
#
#
# class PerevalActivitiesType(Base):
#     __tablename__ = "Perevals"
#
#
# class Coords(Base):
#     __tablename__ = "Perevals"
#
#
# class Level(Base):
#     __tablename__ = "Perevals"
#
#
# class PerevalArea(Base):
#     __tablename__ = "Perevals"
#
#
# class ActivitiesType(Base):
#     __tablename__ = "Perevals"

