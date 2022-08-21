from uuid import uuid4

import factory

from src.entities.document import EsDocument


class DictDocumentFactory(factory.Factory):
    name = factory.Faker("name")
    address = factory.Faker("address")

    class Meta:
        model = dict


class EsDocumentFactory(factory.Factory):
    index = factory.Faker("slug")
    id = factory.LazyAttribute(lambda x: str(uuid4()))
    document = factory.SubFactory(DictDocumentFactory)

    class Meta:
        model = EsDocument
