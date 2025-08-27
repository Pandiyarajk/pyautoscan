.PHONY: help install install-dev test lint format type-check security-check clean build dist upload-pypi

help:  ## Show this help message
	@echo "PyAutoScan Development Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt

install-dev:  ## Install development dependencies
	pip install -r requirements-dev.txt

test:  ## Run tests
	python -m pytest tests/ -v

lint:  ## Run linting checks
	flake8 pyautoscan/ tests/
	black --check pyautoscan/ tests/
	isort --check-only pyautoscan/ tests/

format:  ## Format code with black and isort
	black pyautoscan/ tests/
	isort pyautoscan/ tests/

type-check:  ## Run type checking with mypy
	mypy pyautoscan/

security-check:  ## Run security checks with bandit
	bandit -r pyautoscan/

check-all: lint type-check security-check test  ## Run all checks

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf pyautoscan/__pycache__/
	rm -rf tests/__pycache__/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean  ## Build package
	python -m build

dist: build  ## Create distribution packages
	python -m build --wheel --sdist

upload-pypi: dist  ## Upload to PyPI (requires twine)
	twine upload dist/*

upload-testpypi: dist  ## Upload to TestPyPI (requires twine)
	twine upload --repository testpypi dist/*

install-local: build  ## Install package locally
	pip install dist/*.whl

uninstall-local:  ## Uninstall local package
	pip uninstall pyautoscan -y

run-basic:  ## Run basic scanner
	python -m pyautoscan.basic_scan

run-advanced:  ## Run advanced scanner
	python -m pyautoscan.advanced_scan

run-info:  ## Run scanner info utility
	python -m pyautoscan.scanner_info
