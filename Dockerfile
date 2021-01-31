FROM jupyter/minimal-notebook

RUN python --version

RUN conda install --quiet --yes -c \
     conda-forge docker-py

ADD requirements.txt /jupyter/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    apt-utils \
    gfortran \
    libnlopt-dev \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD test.sh /tests

RUN test.sh