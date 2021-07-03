FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

ENV APP_PATH /app
RUN apk add --update gcc musl-dev libc-dev linux-headers python3-dev libffi-dev  openssl-dev cargo

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY create_superuser.py /

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user