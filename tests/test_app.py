import pytest
import toml
from fastapi.testclient import TestClient

from src.main import app
from tests.entities.factories import EsDocumentFactory


@pytest.fixture
def test_client():
    return TestClient(app())


# == /healthcheck/ tests ==


@pytest.mark.integration
def test_healthcheck_successful(test_client):
    expected_version = (
        toml.load("pyproject.toml").get("tool", {}).get("poetry", {}).get("version")
    )
    response = test_client.get("/healthcheck/")
    assert response.status_code == 200
    assert response.json() == {"version": expected_version}


# == /documents/ tests ==


@pytest.mark.integration
def test_create_document_successful(test_client):
    document = EsDocumentFactory.create(index="test-index").dict()
    response = test_client.post("/documents/", json=document)
    assert response.status_code == 201
    assert response.json().get("result") == "created"


@pytest.mark.integration
def test_create_document_returns_400(test_client):
    document = EsDocumentFactory.create(
        index="test-index",
        document="test-document",
    ).dict()
    response = test_client.post("/documents/", json=document)
    assert response.status_code == 400
