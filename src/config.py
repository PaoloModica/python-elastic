from pydantic import BaseSettings


class Settings(BaseSettings):
    # == Elastic settings ==
    es_host: str = "localhost"
    elastic_user: str = "elastic"
    elastic_password: str

    # == logger settings ==
    logger_level: str = "INFO"
    datefmt: str = "%Y-%m-%d %H:%M:%S"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
