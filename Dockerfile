FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY .env ./src/config.py

RUN rm .env 

CMD [ "python", "/usr/src/app/src/schedulebot.py" ]