import toml
from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    version: str = Field(
        default=toml.load("pyproject.toml")
        .get("tool", {})
        .get("poetry", {})
        .get("version"),
        description="SemVer service version",
    )
