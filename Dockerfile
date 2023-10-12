FROM python:3.10

WORKDIR /code

#COPY requirements.txt .
COPY pyproject.toml .
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
