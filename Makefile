env ?= .env
include $(env)

.PHONY: format lint test-integration test-unit test up

format:
	@poetry run isort .
	@poetry run black src/ tests/

lint:
	@poetry run flake8 --count --show-source src/ tests/

test-integration:
	$(MAKE) start-es
	@sleep 10
	@poetry run pytest -m integration -vvv -s -x --cov=src --cov-report=term-missing tests/
	$(MAKE) stop-es

test-unit:
	@poetry run pytest -m unit -vvv -s -x --cov=src --cov-report=term-missing tests/

test: test-unit test-integration

start-es:
	docker-compose up --build --detach

stop-es:
	docker-compose down -v --remove-orphans


run:
	@poetry run uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

up: start-es
