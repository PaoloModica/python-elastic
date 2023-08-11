from typing import Any, Dict

import elasticsearch
from fastapi import APIRouter, HTTPException

from src.adapters.esclient import ElasticClient
from src.entities.document import EsDocument


def create_router(esclient: ElasticClient) -> APIRouter:
    router = APIRouter(
        prefix="/documents",
        tags=["documents"],
        responses={
            201: {"description": "Created"},
            422: {"description": "Unprocessable entity"},
            500: {"description": "Internal Server Error"},
        },
    )

    @router.post("/", response_model=Dict[str, Any], status_code=201)
    def create_document(body: EsDocument) -> Dict[str, Any]:
        try:
            response = esclient.create(document=body)
            return response
        except elasticsearch.RequestError:
            raise HTTPException(status_code=400, detail="Request Error")
        except elasticsearch.ConflictError:
            raise HTTPException(status_code=409, detail="Conflict")
        except Exception:
            raise HTTPException(status_code=500, detail="Unhandled exception")

    return router
