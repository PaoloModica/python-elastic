import pytest

from src.adapters.esclient import ElasticClient
from src.config import Settings


@pytest.fixture
def logger(mocker):
    return mocker.MagicMock(spec=["critical", "debug", "error", "info", "warning"])


@pytest.fixture
def settings():
    return Settings()


@pytest.fixture
def dummy_elastic_client(logger, settings):
    return ElasticClient(logger=logger, settings=settings)
