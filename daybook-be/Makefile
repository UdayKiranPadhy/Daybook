# Variables
VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
PIP_COMPILE    = $(or $(wildcard $(VENV)/bin/pip-compile), $(shell which pip-compile)) -q --resolver=backtracking --upgrade
PIP_SYNC       = $(or $(wildcard $(VENV)/bin/pip-sync), $(shell which pip-sync))
SYSTEM_PYTHON  = $(or $(shell which python3.10), $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))

# Setup
build: .env venv install-requirements

.env:
	cp .env.dist .env

venv:
	([ '$(SKIP_VENV)' = '1' ] || [ -d '$(VENV)' ]) || $(SYSTEM_PYTHON) -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip wheel setuptools pip-tools

requirements.txt: venv
	CUSTOM_COMPILE_COMMAND="make $@" $(PIP_COMPILE) -o $@ pyproject.toml

requirements-dev.txt: venv
	CUSTOM_COMPILE_COMMAND="make $@" $(PIP_COMPILE) --extra dev -o $@ pyproject.toml

install-requirements: venv
	$(PYTHON) -m pip install -r requirements.txt

install-dev-requirements: venv
	$(PYTHON) -m pip install -r requirements-dev.txt

sync-requirements: venv
	$(PIP_SYNC) requirements.txt

sync-dev-requirements: venv
	$(PIP_SYNC) requirements-dev.txt

clean:
	rm -rf $(VENV)
	find . -iname "*.pyc" -exec rm -rf {} +
	find . -iname "*.egg-info" -exec rm -rf {} +

# Tests
unit-tests:
	$(PYTHON) -m coverage run -m pytest tests/

unit-tests-bitbucket:
	mkdir -p ./test-results
	$(PYTHON) -m coverage run -m pytest --junitxml=./test-results/unit-tests.xml tests/

coverage-xml:
	$(PYTHON) -m coverage xml

BLACK = $(or $(wildcard $(VENV)/bin/black), $(shell which black))
RUFF  = $(or $(wildcard $(VENV)/bin/ruff), $(shell which ruff))
MYPY  = $(or $(wildcard $(VENV)/bin/mypy), $(shell which mypy))
format:
	$(BLACK) src/ tests/ ./cli.py
	$(RUFF) check --fix-only src/ tests/ ./cli.py

lint:
	$(BLACK) --check src/ tests/ ./cli.py
	$(RUFF) check src/ tests/ ./cli.py
	$(MYPY) src/

lint-bitbucket:
	$(BLACK) --check src/ tests/ ./cli.py
	mkdir -p ./test-results
	$(RUFF) check --output-format junit src/ tests/ ./cli.py > ./test-results/ruff.xml
	$(MYPY) --junit-xml ./test-results/mypy.xml src/
