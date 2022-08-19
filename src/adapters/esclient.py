from dataclasses import dataclass
from logging import Logger

import elasticsearch

from src.config import Settings


@dataclass
class ElasticClient:
    logger: Logger
    settings: Settings

    def __post_init__(self):
        try:
            self.esclient = elasticsearch.Elasticsearch(
                hosts=[{"host": self.settings.es_host, "port": 9200}],
                http_auth=(self.settings.elastic_user, self.settings.elastic_password),
                use_ssl=True,
                verify_certs=False,
            )
            # == test connection ==
            self.esclient.ping()
        except Exception as err:
            self.logger.error(
                f"An error occurred while instantiating Elastic client. Error:{err}",
            )
