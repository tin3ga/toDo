FROM python:alpine3.19 as base

RUN pip install --upgrade pip --no-cache-dir

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt  --no-cache-dir

COPY ./todo /app/todo 

WORKDIR /app/todo

ENV SECRET_KEY='supersecretkey'

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "main:app"]

FROM base as test 

RUN pip install -r requirements.txt  --no-cache-dir