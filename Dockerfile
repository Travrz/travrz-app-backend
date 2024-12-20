FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

ARG DEV=false

RUN apt-get update && \
    apt-get install -y \
        gcc \
        python3-dev \
        libpq-dev \
        postgresql-client \
        build-essential \
        musl-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        --gecos '' \
        myuser && \
    chown -R myuser:myuser /app

USER myuser
COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

