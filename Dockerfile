FROM python:3.7

ADD requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /pytest

COPY . .

USER root

WORKDIR ./tests

CMD ["bash"]
