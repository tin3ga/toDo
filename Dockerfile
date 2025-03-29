ARG VERSION=3.12-slim

FROM python:${VERSION} AS builder

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/todo

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./todo ./

ENV SECRET_KEY='supersecretkey'

CMD [ "python", "main.py"]



# Test Stage

FROM builder AS test

WORKDIR /app

COPY ./tests ./tests

RUN pip install pytest --no-cache-dir

WORKDIR /app/tests

CMD [ "pytest"]


# Production Stage

FROM builder AS production

WORKDIR /app/todo 

ENV SECRET_KEY='supersupersecretkey'

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "--workers", "4", "--keep-alive", "5", "main:app"]
