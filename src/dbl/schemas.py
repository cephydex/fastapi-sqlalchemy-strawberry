from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from src.db import Base
import strawberry

@strawberry.type
class ItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    price: float
    description: Optional[str] = None
    store_id: int

class ItemCreate(ItemBase):
    pass


@strawberry.type
class Item(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    description: Optional[str] = None
    store_id: int


# @strawberry.type
# class Item(ItemBase):
#     model_config = ConfigDict(from_attributes=True)

#     id: int


@strawberry.type
class StoreBase(BaseModel):
    name: str

# @strawberry.input
# class StoreCreate(StoreBase):
#     pass


class StoreCreate(StoreBase):
    pass

@strawberry.input
class StoreInput:
    name: str

@strawberry.type
class Store(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    items: List[Item] = []


@strawberry.input
class ItemInput:
    name: str
    price: float
    description: Optional[str] = None
    store_id: int
