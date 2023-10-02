FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/home/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ${APP_HOME}