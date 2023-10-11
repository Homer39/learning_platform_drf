FROM python:3.11

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml

RUN pip install poetry

COPY . .
