from sqlalchemy import Column, Integer, String, Boolean
from sql_app.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(Integer, unique=True)
    is_active = Column(Boolean, default=False)