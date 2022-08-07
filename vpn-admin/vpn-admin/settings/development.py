from .base import *

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("PG_HOST"),
        'PORT': env("PG_PORT"),
    }
}

IMAGE_NAME = "vpn-debian"
NUMBER_CONTAINERS = 10
VPN_PREFIX = "vpn_dion_server_"
LISTEN_PORT = 34078