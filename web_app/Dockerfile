FROM python:3.5

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python3-pip \
    python3-dev \
    python3-psycopg2 \
    musl-dev \
    postgresql-contrib \
    libpq-dev \
    ssh \
    && apt-get autoremove \
    && apt-get clean


ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV PYTHONUSERBASE=/usr/local/

# 파이썬 버전에 따라 중간 경로인 python3.6 부분이 달라집니다.
ENV PATH=${PYTHONUSERBASE}lib/python3.5/site-packages/bin:${PATH}
ENV PYTHONUNBUFFERED=0

# uwsgi 포트
EXPOSE 8001


RUN mkdir /web_app
COPY . /web_app
WORKDIR /web_app

RUN pip install pip --upgrade && \
    pip install setuptools --upgrade && \
    pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh