# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id==user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def get_perevals(db: Session, skip: int=0, limit: int = 100):
#     return db.query(models.Pereval).offset(skip).limit(limit).all()
#
#
# def create_pereval(db: Session, pereval: schemas.PerevalCreate, user_id: int):
#     db_pereval = models.Pereval(**pereval.dict(), user_id=user_id)
#     db.add(db_pereval)
#     db.commit()
#     db.refresh(db_pereval)
#     return db_pereval





