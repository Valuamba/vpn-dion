ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

update-api:
	cd bot; \
	openapi-python-client update --url http://localhost:54340/api/v1/openapi-schema --config ../vpn_client.config; \
	./venv/bin/pip3.8 uninstall -y vpn_api_client; \
	./venv/bin/pip3.8 install ./vpn_api_client;

dev-pg:
	docker compose --env-file .env -f docker-compose.yml run -d --service-ports pg

dev-down:
	docker-compose -f docker-compose.dev.yml down

build:
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f docker-compose.build.yml build

up:
	docker-compose up 

down:
	docker-compose down

show-logs:
	docker-compose logs

migrate:
	docker-compose exec api python3 manage.py migrate

makemigrations:
	docker-compose exec api python3 manage.py makemigrations

superuser:
	docker-compose exec admin python3 manage.py createsuperuser

collectstatic:
	docker-compose exec api python3 manage.py collectstatic --no-input --clear

import-tariffs:
	docker-compose exec admin python3 manage.py import_tariffs

mock-sub-data:
	docker-compose exec admin python3 manage.py mock_sub_data

import_locales:
	docker-compose exec admin python3 manage.py import_bot_locales

down-v:
	docker-compose down -v

volume:
	docker volume inspect estate-src_postgres_data
