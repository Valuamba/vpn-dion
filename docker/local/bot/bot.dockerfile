FROM ubuntu:20.04

WORKDIR /srv

RUN apt-get update && apt-get install -y gfortran  libpq-dev gcc libopenblas-dev liblapack-dev pip python netcat
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y language-pack-ru
ENV LANGUAGE ru_RU.UTF-8
RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales


COPY bot/requirements.txt .
RUN pip install -U pip
RUN --mount=type=cache,target=/root/.cache \
    pip install -Ur requirements.txt

COPY bot .
# RUN pip install /srv/vpn_api_client;

COPY .env .env
COPY scripts scripts

RUN ["chmod", "+x", "./scripts/docker-entrypoint.bot.sh"]
RUN ["chmod", "+x", "./scripts/wait-for.sh"]
CMD ["./scripts/docker-entrypoint.bot.sh"]