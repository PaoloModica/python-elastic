from dataclasses import dataclass
from logging import Logger
from typing import Any, Dict

import elasticsearch

from src.config import Settings
from src.entities.document import EsDocument


@dataclass
class ElasticClient:
    logger: Logger
    settings: Settings

    def __post_init__(self):
        try:
            self.esclient = elasticsearch.Elasticsearch(
                hosts=[{"host": self.settings.es_host, "port": 9200}],
                http_auth=(self.settings.elastic_user, self.settings.elastic_password),
                verify_certs=False,
            )
            # == test connection ==
            self.esclient.ping()
        except Exception as err:
            self.logger.error(
                f"An error occurred while instantiating Elastic client. Error:{err}",
            )

    def create(self, document: EsDocument) -> Dict[str, Any]:
        """
        Creates or updates a document in an Elasticsearch index,
        exploiting the information packed in the EsDocument instance
        provided in input.
        Returns the response provided by the service

        Args:
            document (EsDocument): instance containing the document to index within
            ElasticSearch.

        Returns:
            Dict[str, Any]: Elasticseach response.
        """
        response = self.esclient.index(
            index=document.index,
            id=document.id,
            body=document.document,
            refresh="true",
        )
        if not response:
            err_message = "Document indexing failed."
            self.logger.error(err_message)
            raise Exception(err_message)
        return response
