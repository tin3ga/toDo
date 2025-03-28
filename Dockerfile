ARG VERSION=3.12-slim

FROM python:${VERSION} AS builder

RUN pip install --upgrade pip --no-cache-dir

WORKDIR /app/todo

COPY requirements.txt ./

RUN pip install -r requirements.txt  --no-cache-dir

COPY ./todo ./

ENV SECRET_KEY='supersecretkey'

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "main:app"]