FROM --platform=linux/amd64 python:3.10-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /edent

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . . 

CMD python manage.py runserver 0.0.0.0:8000