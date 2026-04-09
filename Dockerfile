FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Works both locally and in Cloud Run
CMD exec gunicorn --bind :${PORT:-8080} app:app
