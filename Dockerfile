FROM python:3.12-slim AS builder

RUN pip install --upgrade pip --no-cache-dir

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt  --no-cache-dir

COPY ./todo /app/todo 

WORKDIR /app/todo

ENV SECRET_KEY='supersecretkey'

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "main:app"]

# Test Stage

FROM builder as test 

COPY ./todo /app/todo

WORKDIR /app/tests

RUN pip install pytest --no-cache-dir

COPY ./tests /app/tests

CMD ["pytest"]