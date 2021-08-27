FROM python:3.9.6

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY . .
RUN chmod +x setup.sh
RUN ./setup.sh


CMD [ "python", "./app.py"]
