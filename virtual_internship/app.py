from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql_app.utils import get_db
from . import service
from .schemas import PerevalCreate


router = APIRouter()


@router.get('/')
def get_pereval_list(db: Session = Depends(get_db)):
    pereval = service.get_pereval_list(db)
    return pereval


@router.post('/')
def create_pereval(item: PerevalCreate, db: Session = Depends(get_db)):
    return service.create_pereval(db, item)

