env ?= .env
include $(env)

.PHONY: up

start-es:
	docker-compose up --build --detach

stop-es:
	docker-compose down -v --remove-orphans
