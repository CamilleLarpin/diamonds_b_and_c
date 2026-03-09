# Usage: make <target>

lint:
	ruff check . --fix && ruff format .

train:
	python -m diamonds.train

test:
	pytest src/tests/
