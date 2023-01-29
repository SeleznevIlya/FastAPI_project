from sqlalchemy.orm import Session
from .models import Pereval
from .schemas import PerevalCreate


def get_pereval_list(db: Session):
    return db.query(Pereval).all()


def create_pereval(db: Session, item: PerevalCreate):
    pereval = Pereval(**item.dict())
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval