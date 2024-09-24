from typing import List, Optional
from src.dbl.repositories import StoreRepo, ItemRepo
from src.dbl import models, schemas
import logging

logger = logging.getLogger(__name__)
from sqlalchemy.orm import Session
import strawberry


class StoreQueries:

    def __init__(self) -> None:
        pass


    def get_all_stores(self, info: strawberry.Info) -> List[schemas.Store]:
        db: Session = info.context["db"]
        return StoreRepo.fetch_all(db)


    def get_single_store(self, info: strawberry.Info, id: int) -> Optional[schemas.Store]:
        db: Session = info.context["db"]
        return StoreRepo.fetch_by_id(db, id)


class ItemQueries:
    def get_all_items(self, info: strawberry.Info) -> List[schemas.Item]:
        db: Session = info.context["db"]
        return ItemRepo.fetch_all(db)
    

    def get_single_item(self, info: strawberry.Info, id: int) -> Optional[schemas.Item]:
        db: Session = info.context["db"]
        return ItemRepo.fetch_by_id(db, id)
    

class CtrlMutation:

    def add_store(self, info, store_data: schemas.StoreInput) -> schemas.Store:
        db = info.context["db"]
        # data = schemas.StoreCreate(name=store_data.name)
        logger.info("CMD :: add store")
        
        return StoreRepo.create(db, store_data)

    def add_item(self, info, item_data: schemas.ItemInput) -> schemas.Store:
        db = info.context["db"]
        logger.info("CMD :: add item")

        return ItemRepo.create(db, item_data)
