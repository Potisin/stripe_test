FROM python:3.10.6-alpine3.15

WORKDIR /app/
COPY Pipfile  /app/backend/
COPY Pipfile.lock /app/backend/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=1


WORKDIR /app/backend
RUN pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile


COPY . .

