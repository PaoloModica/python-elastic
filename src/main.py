from fastapi import FastAPI

import src.adapters.routers.healthcheck as healthcheck
from src.adapters.esclient import ElasticClient
from src.adapters.routers.document import create_router as create_document_router
from src.config import Settings
from src.logger import create_logger


def app():
    # == initialise application components ==
    settings = Settings()
    logger = create_logger(settings=settings)
    es_client = ElasticClient(logger=logger, settings=settings)
    document_router = create_document_router(esclient=es_client)

    fastapi_app = FastAPI()

    fastapi_app.include_router(healthcheck.router)
    fastapi_app.include_router(document_router)

    return fastapi_app
