from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from src.db import get_db
from src.dbl import schemas
from src.dbl.repositories import ItemRepo
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix="/api/v1", tags=["item"])


@router.post('/items',response_model=schemas.Item,status_code=201)
async def create_item(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """
    
    db_item = ItemRepo.fetch_by_name(db, name=item_request.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await ItemRepo.create(db=db, item=item_request)


@router.get('/items',response_model=List[schemas.Item])
def get_all_items(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the Items stored in database
    """
    if name:
        items = []
        db_item = ItemRepo.fetch_by_name(db,name)
        items.append(db_item)
        return items
    else:
        return ItemRepo.fetch_all(db)


@router.put('/items/{item_id}',response_model=schemas.Item)
async def update_item(item_id: int,item_request: schemas.Item, db: Session = Depends(get_db)):
    db_item = ItemRepo.fetch_by_id(db, item_id)
    if db_item:
        update_item_encoded = jsonable_encoder(item_request)
        db_item.name = update_item_encoded['name'] if update_item_encoded['name'] else db_item.name
        db_item.price = update_item_encoded['price'] if update_item_encoded['price'] else db_item.price
        db_item.description = update_item_encoded['description'] if update_item_encoded['description'] else db_item.description
        db_item.store_id = update_item_encoded['store_id'] if update_item_encoded['store_id'] else db_item.store_id
        return await ItemRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")
