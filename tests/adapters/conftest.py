import pytest

from src.config import Settings


@pytest.fixture
def logger(mocker):
    return mocker.MagicMock(spec=["critical", "debug", "error", "info", "warning"])


@pytest.fixture
def settings():
    return Settings()
