# syntax=docker/dockerfile:1
FROM python:3.11.3-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app

# install app dependencies
RUN pip install --upgrade pip
COPY  ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

# RUN python populate_db.py


# final configuration
EXPOSE 8000
# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]