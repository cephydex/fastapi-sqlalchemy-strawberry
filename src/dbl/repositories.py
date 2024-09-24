from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

class ItemRepo:

    async def create(db: Session, item: schemas.ItemCreate):
        db_item = models.Item(name=item.name, price=item.price, description=item.description, store_id=item.store_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    

    def fetch_by_id(db: Session, _id: int) -> schemas.Item:
        return db.query(models.Item).filter(models.Item.id==_id).first()
    

    def fetch_by_name(db: Session, name: str):
        return db.query(models.Item).filter(models.Item.name==name).first()
    

    def fetch_all(db: Session, skip: int = 0, limit:int = 100):
        return db.query(models.Item).offset(skip).limit(limit).all()
    

    async def update(db:Session, item_data):
        updated_item = db.merge(item_data)
        db.commit()
        return updated_item
    
    async def delete(db: Session,item_id):
        db_item= db.query(models.Item).filter_by(id=item_id).first()
        db.delete(db_item)
        db.commit()


class StoreRepo:

    async def create(db: Session, store: schemas.StoreCreate):
        db_item = models.Store(name=store.name)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    

    def fetch_by_id(db: Session, _id: int) -> schemas.Store:
        return db.query(models.Store).filter(models.Store.id==_id).first()
    

    def fetch_by_name(db: Session, name: str):
        return db.query(models.Store).filter(models.Store.name==name).first()
    

    # def fetch_all(db: Session, skip: int = 0, limit:int = 100) -> List[models.Store]:
    def fetch_all(db: Session, skip: int = 0, limit:int = 100) -> List[schemas.Store]:
        print("CHECK FIRST", db)
        return db.query(models.Store).offset(skip).limit(limit).all()
    

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Store).offset(skip).limit(limit).all()
    
    async def delete(db: Session,_id:int):
        db_store= db.query(models.Store).filter_by(id=_id).first()
        db.delete(db_store)
        db.commit()
        
    async def update(db: Session,store_data):
        db.merge(store_data)
        db.commit()