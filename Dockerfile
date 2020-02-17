FROM python:3.6

ENV PYTHONNUNBUFFERED 1

RUN mkdir /app_docker

# Create app directory
WORKDIR /app_docker

COPY . /app_docker

RUN pip install -r requirements.txt

COPY ./bin/settings.py app/bin
