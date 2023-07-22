import json

import pytest
from elasticmock import elasticmock

from src.adapters.esclient import ElasticClient
from tests.entities.factories import DictDocumentFactory, EsDocumentFactory

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


# == create() tests ==

test_dict_document = DictDocumentFactory.create()

create_test_cases = [
    pytest.param(
        EsDocumentFactory.create(
            index="test-index", document=json.dumps(test_dict_document)
        ),
        id="string document, specified ID",
    ),
    pytest.param(
        EsDocumentFactory.create(index="test-index", document=test_dict_document),
        id="dict document, specified ID",
    ),
    pytest.param(
        EsDocumentFactory.create(
            index="test-index", id=None, document=json.dumps(test_dict_document)
        ),
        id="string document, no ID",
    ),
    pytest.param(
        EsDocumentFactory.create(
            index="test-index", id=None, document=test_dict_document
        ),
        id="dict document, no ID",
    ),
]


@elasticmock
@pytest.mark.parametrize("document_param", create_test_cases)
@pytest.mark.unit
def test_create_successful(document_param, dummy_elastic_client):
    response = dummy_elastic_client.create(document=document_param)
    assert isinstance(response, dict)
    assert response.get("_index") == document_param.index


@pytest.mark.parametrize("document_param", create_test_cases)
@pytest.mark.integration
def test_create_integration_successful(document_param, dummy_elastic_client):
    response = dummy_elastic_client.create(document=document_param)
    assert isinstance(response, dict)
    assert response.get("_index") == document_param.index
    assert response.get("result") == "created"


@pytest.mark.integration
def test_create_text_document_not_parsable_raise_error(dummy_elastic_client):
    document_param = EsDocumentFactory.create(document="test_document")
    with pytest.raises(Exception):
        dummy_elastic_client.create(document=document_param)
