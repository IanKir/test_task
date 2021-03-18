FROM python:3

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt
