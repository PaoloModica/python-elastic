env ?= .env
include $(env)

.PHONY: format lint test-integration test-unit test up

format:
	@python -m isort .
	@python -m black src/ tests/

lint:
	@python -m flake8 --count --show-source src/ tests/

test-integration:
	$(MAKE) start-es
	@sleep 5
	@python -m pytest -m integration -vvv -s -x --cov=src --cov-report term-missing tests/
	$(MAKE) stop-es

test-unit:
	@python -m pytest -m unit -vvv -s -x --cov=src --cov-report term-missing tests/

test: test-unit test-integration

start-es:
	docker-compose up --build --detach

stop-es:
	docker-compose down -v --remove-orphans

up: start-es
