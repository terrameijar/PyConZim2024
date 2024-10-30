# syntax=docker/dockerfile:1
FROM python:3.11.3-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl

# Create a non-root user and switch to it
# RUN useradd -m appuser
# USER appuser

# install app dependencies
COPY  ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app/


# final configuration
EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]