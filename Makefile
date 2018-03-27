test: lint test-python

lint:
	@echo ""

test-python:
	@echo "Running tests"
	python manage.py test

server:
	python manage.py runserver


server-prod:
	gunicorn src.server:app
