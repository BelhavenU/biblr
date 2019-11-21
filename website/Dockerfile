FROM python:3.7-slim

RUN mkdir /website

WORKDIR /website

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP website.app:create_app()
ENV FLASK_ENV development
CMD flask run -h 0.0.0.0
