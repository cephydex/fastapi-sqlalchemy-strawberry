from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src import item_router, store_router
import strawberry
import logging, os
from strawberry.fastapi import GraphQLRouter
from src.gql.query_schema import Query
from src.gql.mutation_schema import Mutation
from src.application import create_app
from src.db import get_db


log_level = logging.INFO
if os.environ.get("DEBUG"):
    log_level = logging.DEBUG
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S%p"
)
logger = logging.getLogger(__name__)


app = create_app()

@app.exception_handler(Exception)
def exception_handler(req, err):
    base_error_msg = f"Failed to execute {req.method} : {req.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_msg}. Detail: {err}"})


app.include_router(item_router)
app.include_router(store_router)

def get_context(db:Session =Depends(get_db)):
    logger.info(db)
    return {'db': db}

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
graphgql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphgql_app, prefix="/graphql")


@app.get("/")
def index():
    return {"message": "Service is live!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
