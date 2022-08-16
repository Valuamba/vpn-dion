FROM ubuntu:20.04

WORKDIR /srv


RUN apt-get update && apt-get install -y gfortran  libpq-dev gcc libopenblas-dev liblapack-dev pip python netcat
RUN apt-get update
RUN apt-get upgrade -y

# RUN apk add git curl openssh
# RUN apk add jpeg-dev zlib-dev postgresql-dev

COPY vpn-admin /srv/
RUN pip install -U pip
RUN pip install -Ur /srv/requirements.txt

COPY scripts scripts

RUN ["chmod", "+x", "./scripts/docker-entrypoint.admin.sh"]
RUN ["chmod", "+x", "./scripts/wait-for.sh"]
CMD ["./scripts/docker-entrypoint.admin.sh"]