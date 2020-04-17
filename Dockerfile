FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8080:8080
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN django-admin startproject frontend
COPY . /app/
CMD python frontend/manage.py runserver
