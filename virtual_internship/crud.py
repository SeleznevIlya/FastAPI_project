from sqlalchemy.orm import Session
from .models import Pereval
from .schemas import PerevalCreate


def get_pereval_list(db: Session):
    """Получаем список всех перевалов"""
    return db.query(Pereval).all()


def get_pereval(db: Session, pk: int):
    """"Получаем конкретный перевал по pk"""
    return db.query(Pereval).get(pk)


def create_pereval(db: Session, item: PerevalCreate):
    """Создаем объект перевала"""
    pereval = Pereval(**item.dict())
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval