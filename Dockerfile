FROM python:3.7.3-stretch

RUN apt-get update

WORKDIR /thoth

COPY pyproject.toml .

RUN poetry install

COPY . .

ENTRYPOINT [ "poetry", "run", "manage.py" "runserver" ]
