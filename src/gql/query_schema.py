import strawberry
from .controllers import StoreQueries, ItemQueries
from src.dbl import schemas
from typing import List

# from src.dbl.repositories import StoreRepo
# from sqlalchemy.orm import Session

@strawberry.type
class Query:
    get_all_stores: List[schemas.Store] = strawberry.field(StoreQueries.get_all_stores)
    get_single_store = strawberry.field(resolver=StoreQueries.get_single_store)
    get_all_items: List[schemas.Item] = strawberry.field(ItemQueries.get_all_items)
    get_single_item = strawberry.field(resolver=ItemQueries.get_single_item)

    @strawberry.field
    def hello() -> str:
        return "Hello to queries"
    
    # @strawberry.field
    # def all_stores(self, info) -> List[schemas.Store]:
    #     # print('CONTEXT', info.context["db"])
    #     db: Session = info.context["db"]
    #     return StoreRepo.fetch_all(db)