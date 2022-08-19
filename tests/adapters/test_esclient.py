import pytest
from elasticmock import elasticmock

from src.adapters.esclient import ElasticClient

# == ElasticClient build tests ==


@elasticmock
@pytest.mark.unit
def test_elasticclient_build_successful(logger, settings):
    elastic_client = ElasticClient(logger=logger, settings=settings)
    assert isinstance(elastic_client, ElasticClient)
    assert getattr(elastic_client, "esclient") is not None


@elasticmock
@pytest.mark.unit
def test_elasticclient_connection_raises_error(logger, mocker, settings):
    mocker.patch("elasticsearch.Elasticsearch", side_effect=Exception())
    ElasticClient(logger=logger, settings=settings)
    logger.error.assert_called_once()


@pytest.mark.integration
def test_elasticclient_build_connection_successful(logger, settings):
    elastic_client = ElasticClient(logger=logger, settings=settings)
    assert isinstance(elastic_client, ElasticClient)
    assert elastic_client.esclient.info()
