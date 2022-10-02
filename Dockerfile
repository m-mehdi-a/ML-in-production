FROM python:3.9-slim-bullseye

RUN apt-get -y update && apt-get -y install nginx

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY inference.py ./inference.py
COPY api.py ./api.py



