FROM python:3.7-slim-buster

ADD . /app

WORKDIR /app

RUN apt update && apt install -y gcc g++
RUN pip install -r requirements.txt && python -m spacy download en

EXPOSE 5000/tcp

ENTRYPOINT python app.py