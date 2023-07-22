import json

import pytest

from src.entities.document import EsDocument

dict_document = {
    "name": "John Doe",
    "address": "42 Wallaby Way, Sydney",
}
esdocument_test_cases = [
    pytest.param(
        {
            "index": "customer",
            "id": "01234",
            "document": json.dumps(dict_document),
        },
        id="string document, specified ID",
    ),
    pytest.param(
        {
            "index": "customer",
            "id": "01234",
            "document": dict_document,
        },
        id="dict document, specified ID",
    ),
    pytest.param(
        {
            "index": "customer",
            "document": json.dumps(dict_document),
        },
        id="string document, no ID",
    ),
    pytest.param(
        {
            "index": "customer",
            "document": dict_document,
        },
        id="dict document, no ID",
    ),
]


@pytest.mark.parametrize("es_document_param", esdocument_test_cases)
@pytest.mark.unit
def test_esdocument_build_successful(es_document_param):
    esdocument = EsDocument(**es_document_param)
    assert isinstance(esdocument, EsDocument)
    assert esdocument.id == es_document_param.get("id")
