from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from src.db import get_db
from src.dbl import schemas
from src.dbl.repositories import StoreRepo
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["Store"])


@router.post('/stores', response_model=schemas.Store,status_code=201)
async def create_store(store_request: schemas.StoreCreate, db: Session = Depends(get_db)):
    """
    Create a Store and save it in the database
    """
    db_store = StoreRepo.fetch_by_name(db, name=store_request.name)
    print(db_store)
    if db_store:
        raise HTTPException(status_code=400, detail="Store already exists!")

    return await StoreRepo.create(db=db, store=store_request)

@router.get('/stores', response_model=List[schemas.Store])
def get_all_stores(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the Stores stored in database
    """
    if name:
        stores =[]
        db_store = StoreRepo.fetch_by_name(db,name)
        print(db_store)
        stores.append(db_store)
        return stores
    else:
        return StoreRepo.fetch_all(db)
    

@router.get('/stores/{store_id}', response_model=schemas.Store)
def get_store(store_id: int,db: Session = Depends(get_db)):
    """
    Get the Store with the given ID provided by User stored in database
    """
    db_store = StoreRepo.fetch_by_id(db,store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found with the given ID")
    return db_store


@router.put('/stores/{store_id}', response_model=schemas.Store)
async def get_store(store_id: int, store_req: schemas.Store, db: Session = Depends(get_db)):
    db_store = StoreRepo.fetch_by_id(db, store_id)
    if db_store:
        update_store_encoded = jsonable_encoder(store_req)
        db_store.name = update_store_encoded["name"]
        logger.warning("JSON ENC")
        logger.warning(update_store_encoded)
        
        return await StoreRepo.update(db, db_store)

    raise HTTPException(status_code=404, detail="Store not found with the given ID")
