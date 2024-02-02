FROM python:3.8

WORKDIR /scheduler

COPY scheduler/ ./
COPY utils/ ./utils

RUN pip3 install -r requirements.txt

CMD [ "python3", "scheduler.py"]