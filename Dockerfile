# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 - && \
    /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install --no-dev --no-root