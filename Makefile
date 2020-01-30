NAME=flaskapp

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

local:
	docker-compose -f docker-compose-local.yml up -d

run:
	docker-compose build
	docker-compose up -d

stop:
	docker-compose down