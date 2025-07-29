install:
	pip install -r requirements.txt

test:
	python -m pytest -s test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C,no-value-for-parameter *.py

all: install test format lint