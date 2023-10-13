FROM python:3.11.6-alpine3.18

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY ./app /app

WORKDIR /app

# set default env variables
ENV MONGO_USERNAME=username
ENV MONGO_PASSWORD=password
ENV MONGO_ADDRESS=mongo
ENV MONGO_PORT=27017
ENV MONGO_DATABASE=spotify

RUN pytest

CMD [ "python", "app.py" ]