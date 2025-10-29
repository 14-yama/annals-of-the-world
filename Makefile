install:
	pip install -r requirements.txt -r requirements-dev.txt

lint:
	flake8 src/ tests/

typecheck:
	mypy src/

test:
	pytest tests/
