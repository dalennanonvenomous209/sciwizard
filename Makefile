.PHONY: run test lint typecheck clean install

install:
	pip install -e ".[dev]"

run:
	python -m sciwizard

test:
	pytest tests/ -v --tb=short

lint:
	ruff check sciwizard/ tests/

typecheck:
	mypy sciwizard/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf dist/ build/ *.egg-info/ .pytest_cache/ .mypy_cache/ .ruff_cache/

icon:
	python icon/generate_icon.py
