ARG VERSION=3.13-alpine

FROM python:${VERSION} AS builder

# Install required system dependencies
RUN apk update && apk add \
    libpq-dev libpq build-base linux-headers && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/todo

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


# Development Stage
FROM python:${VERSION} AS development

LABEL org.opencontainers.image.authors="tin3ga"
LABEL org.opencontainers.image.description="Container image for https://github.com/tin3ga/toDo"

RUN apk update \
    && apk upgrade \
    && apk add --no-cache libpq

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

WORKDIR /app/todo

COPY ./todo ./

EXPOSE 5000

CMD [ "python", "main.py"]



# Test Stage

FROM builder AS test

WORKDIR /app

COPY ./tests ./tests

RUN pip install pytest --no-cache-dir

WORKDIR /app/tests

CMD [ "pytest"]


