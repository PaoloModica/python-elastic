# python-elastic

## Overview

A simple project to get my hands on Elastic Stack and learn how to work with it.

## Project details

The project is based on `Python` `3.9.x`.
Project dependencies are managed using [poetry](https://python-poetry.org/).

## Development

### Linting and formatting

The project leverages on [flake8](https://flake8.pycqa.org/en/latest/) for style enforcement and static analysis.
Run style analysis with:
```
make lint
```

[black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/) are exploited for code formatting.
Run code formatting with:
```
make format
```

### Tests

Run tests with `pytest`, showing also source code coverage.

```
make test
```

### Run the application

Run ElasticSearch container with

```
make start-es
```

then, run the FastAPI web service

```
make run
```

## Resources

The project exploits the tutorial provided by Elastic documentation on how to [start a multi node Elasticsearch cluster with Docker Compose](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file).

## License

[MIT License](https://opensource.org/licenses/MIT).