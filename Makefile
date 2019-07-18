.PHONY: install assets

SHELL := /bin/bash

install:
	sudo sh build.sh
	curl -sSL https\://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	poetry install
	touch db/thoth.db

assets:
	cd app ; yarn run build
