import strawberry
from src.dbl import schemas
from src.dbl.repositories import StoreRepo
from .controllers import CtrlMutation
import logging

logger = logging.getLogger(__name__)


@strawberry.type
class Mutation:
    add_single_store: schemas.Store = strawberry.mutation(resolver=CtrlMutation.add_store)
    add_single_item: schemas.Store = strawberry.mutation(CtrlMutation.add_item)
