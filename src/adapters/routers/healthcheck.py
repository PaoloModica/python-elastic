from typing import Any, Dict

from fastapi import APIRouter

from src.entities.health import HealthCheck

router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
    responses={
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)


@router.get("/", response_model=HealthCheck)
def healthcheck() -> Dict[str, Any]:
    return HealthCheck().dict()
