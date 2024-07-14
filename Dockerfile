FROM python:3.8-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    pip install django-cors-headers &&\
    pip install psycopg2-binary