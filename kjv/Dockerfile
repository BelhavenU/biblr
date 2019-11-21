FROM python:3.7-slim

RUN mkdir /kjv

WORKDIR /kjv

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install -U -e .

ENV FLASK_APP kjv.app:create_app()
ENV FLASK_ENV development
CMD flask run -h 0.0.0.0
