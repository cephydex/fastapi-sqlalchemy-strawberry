from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(
        title="Backend Service",
        description="Webservice code",
        version="1.0.0",
    )

    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app