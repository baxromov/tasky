FROM python:3.9-slim-buster

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
COPY entrypoint.sh /code/
RUN chmod +x entrypoint.sh
EXPOSE 8000
