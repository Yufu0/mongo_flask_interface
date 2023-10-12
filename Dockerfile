FROM python:3.11.6-alpine3.18

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY ./app /app

WORKDIR /app

#RUN pytest

CMD [ "python", "app.py" ]