FROM python:alpine3.19

RUN pip install --upgrade pip --no-cache-dir

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt  --no-cache-dir

COPY ./todo /app/todo 

WORKDIR /app/todo

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "main:app"]