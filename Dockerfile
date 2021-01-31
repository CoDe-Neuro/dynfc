FROM python:3.7

WORKDIR .

RUN pip install -r requirements.txt

ADD test.sh /tests

RUN test.sh
