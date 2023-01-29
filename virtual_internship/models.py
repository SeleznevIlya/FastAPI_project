from sql_app.database import Base
from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, DateTime, Float
from sqlalchemy.orm import relationship
#from user.models import User
from sql_app.base import User


class Pereval(Base):
    __tablename__ = "Perevals"

    id = Column(Integer, primary_key=True, unique=True)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship(User)
    beauty_title = Column(String, unique=True)
    title = Column(String)
    other_title = Column(String)
    connect = Column(String)
    add_time = Column(DateTime)

    coodrs = Column(Integer, ForeignKey('coords.id'))
    coords_id = relationship("Coords")

    level = Column(Integer, ForeignKey('level.id'))
    level_id = relationship("Level")

    pereval_area = Column(Integer, ForeignKey('pereval_area.id'))
    pereval_area_id = relationship('PerevalArea')
    # image = Column()


# class PerevalImage(Base):
#     __tablename__ = "pereval_image"
#

# class PerevalActivitiesType(Base):
#     __tablename__ = "Perevals"


class Coords(Base):
    __tablename__ = "coords"

    id = Column(Integer, primary_key=True, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Integer)


class Level(Base):
    __tablename__ = "level"

    id = Column(Integer, primary_key=True, unique=True)
    winter_level = Column(String)
    spring_level = Column(String)
    summer_level = Column(String)
    autumn_level = Column(String)


class PerevalArea(Base):
    __tablename__ = "pereval_area"

    id = Column(Integer, primary_key=True, unique=True)
    area_name = Column(String)



# class ActivitiesType(Base):
#     __tablename__ = "Perevals"

