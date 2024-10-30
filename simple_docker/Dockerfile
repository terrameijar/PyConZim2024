# syntax=docker/dockerfile:1

FROM python:3.14-rc-alpine


RUN pip install flask==3.0.*

COPY . /

ENV FLASK_APP=pyconzim
EXPOSE 8001

ENTRYPOINT ["flask", "run"]
CMD ["--host", "0.0.0.0", "--port", "8001"]