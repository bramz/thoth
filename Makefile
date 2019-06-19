.PHONY: install assets

SHELL := /bin/bash

install:
	$(shell sudo sh build.sh)
	$(shell curl -sSL https\://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python)
	$(shell poetry install)

assets:
	yarn run build
