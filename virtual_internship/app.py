from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql_app.utils import get_db
from user.schemas import UserCreate
from . import crud
from .schemas import PerevalCreate, PerevalList, PerevalUpdate
from typing import List


router = APIRouter()


@router.get('/', response_model=List[PerevalList])
def get_pereval_list(db: Session = Depends(get_db)):
    return crud.get_pereval_list(db)


@router.get('/{pk}/')
def get_pereval(pk: int, db: Session = Depends(get_db)):
    return crud.get_pereval(db, pk)


@router.put('/{pk}/')
def update_pereval(pk: int, item: PerevalUpdate):
    return crud.update_pereval(pk, item)


@router.post('/')
def create_pereval(item: PerevalCreate, db: Session = Depends(get_db)):
    return crud.create_pereval(db, item)


@router.post('/user')
def create_user(item: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, item)

