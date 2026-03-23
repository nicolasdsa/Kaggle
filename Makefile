PYTHON ?= python3
PROJECT ?= lego_database

.PHONY: install dev lint format test new download build-dataset train

install:
	$(PYTHON) -m pip install -e .

dev:
	$(PYTHON) -m pip install -e ".[dev]"

lint:
	ruff check .

format:
	ruff format .

test:
	pytest

new:
	$(PYTHON) -m kaggle_lab.cli.new_project $(PROJECT)

download:
	$(PYTHON) -m projects.$(PROJECT).src.dataset download

build-dataset:
	$(PYTHON) -m projects.$(PROJECT).src.dataset build

train:
	$(PYTHON) -m projects.$(PROJECT).src.train

