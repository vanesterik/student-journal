.PHONY: help run clean format lint
DEFAULT_GOAL := help

help:
	@echo "make build"
	@echo "       build static site"
	@echo "make format"
	@echo "       format all python code"
	@echo "make lint"
	@echo "       lint all python code"
	@echo "make run"
	@echo "       run dev server"
	@echo "make serve"
	@echo "       run build and serve static"
	@echo "make test"
	@echo "       test all python code"

build:
	pdm run python build.py

format:
	pdm run black app tests
	pdm run isort app tests

lint:
	pdm run ruff app tests
	pdm run mypy app tests

run:
	pdm run python run.py

serve:
	make build
	pdm run python -m http.server --directory app/build

test:
	pdm run pytest tests