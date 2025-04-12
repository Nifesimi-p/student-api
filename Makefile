run:
	@flask run

migrate:
	@flask db migrate -m "migration"

upgrade:
	@flask db upgrade

test:
	pytest

setup:
	pip install -r requirements.txt
