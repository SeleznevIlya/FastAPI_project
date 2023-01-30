from sqlalchemy.orm import Session
from sqlalchemy import update
from .models import Pereval
from .schemas import PerevalCreate, PerevalUpdate
from sql_app.database import engine
from user.schemas import UserCreate
from user.models import User


def get_pereval_list(db: Session):
    """Получаем список всех перевалов"""
    return db.query(Pereval).all()


def get_pereval(db: Session, pk: int):
    """"Получаем конкретный перевал по pk"""
    print(db.query(Pereval).get(pk))

    return db.query(Pereval).get(pk)


def update_pereval(pk: int, item: PerevalUpdate):
    """Редактируем объект перевала"""
    with Session(engine) as db:
        pereval = db.get(Pereval, pk)
        pereval_data = item.dict()
        for key, value in pereval_data.items():
            setattr(pereval, key, value)
        db.add(pereval)
        db.commit()
        db.refresh(pereval)
        return pereval


def create_user(db: Session, item: UserCreate):
    user = User(**item.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_pereval(db: Session, item: PerevalCreate):
    """Создаем объект перевала"""
    pereval = Pereval(**item.dict())
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval