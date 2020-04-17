FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8080:8080
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD python frontend/manage.py runserver 8080
