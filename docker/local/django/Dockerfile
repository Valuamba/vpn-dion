FROM ubuntu:20.04

ENV APP_HOME=/srv
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y gfortran  libpq-dev gcc libopenblas-dev liblapack-dev pip python netcat curl vim
RUN apt-get install -y build-essential
RUN apt-get update
RUN apt-get upgrade -y

# RUN apk add git curl openssh
# RUN apk add jpeg-dev zlib-dev postgresql-dev

COPY .env /.env
COPY assets /assets
COPY vpn-admin/requirements.txt /srv/
# COPY vpn-admin /srv/
RUN pip install -U pip
RUN --mount=type=cache,target=/root/.cache \
    pip install -r /srv/requirements.txt
RUN mkdir /srv/logs

COPY scripts /scripts

RUN ["chmod", "+x", "/scripts/docker-entrypoint.admin.sh"]
RUN ["chmod", "+x", "/scripts/wait-for.sh"]
CMD ["./scripts/docker-entrypoint.admin.sh"]
