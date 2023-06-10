SHELL=/bin/bash

.PHONY: airflow-init
airflow-init:
	docker-compose up airflow-init

.PHONY: docker-compose-up
docker-compose-up:
	docker-compose up