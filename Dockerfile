FROM python:3.11

WORKDIR /code

COPY ./pyproject.toml /code/

RUN pip install poetry

RUN poetry install

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
