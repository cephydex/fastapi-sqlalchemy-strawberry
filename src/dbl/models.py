from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from src.db import Base
import strawberry


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    price = Column(Float(precision=2), nullable=False)
    description = Column(String(200))
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)

    def repr(self):
        return 'ItemModel(name=%s, price=%s, store_id=%s)' % (self.name, self.price, self.store_id)


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    items = relationship('Item', cascade="all, delete-orphan")
    # items = relationship('Item', primaryJoin="Store.id == Item.store_id", cascade="all, delete-orphan")

    def repr(self):
        return 'StoreModel(name=%s)' % (self.name)