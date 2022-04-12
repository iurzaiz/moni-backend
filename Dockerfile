FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code/

COPY requirements.txt /code/


RUN python -m pip install -r requirements.txt
RUN python -m pip install requests
RUN python -m pip install django-cors-headers
RUN python -m pip install djangorestframework-simplejwt
RUN python -m pip install markdown
COPY . /code/
