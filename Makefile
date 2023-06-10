SHELL=/bin/bash

# Run airflow
.PHONY: airflow-init
airflow-init:
	docker-compose up airflow-init

.PHONY: docker-compose-build
docker-compose-build:
	docker-compose build

.PHONY: docker-compose-up
docker-compose-up:
	docker-compose up --build