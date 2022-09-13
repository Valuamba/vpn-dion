from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': env("POSTGRES_ENGINE"),
#         'NAME': env("POSTGRES_DB"),
#         'USER': env("POSTGRES_USER"),
#         'PASSWORD': env("POSTGRES_PASSWORD"),
#         'HOST': env("PG_HOST"),
#         'PORT': env("PG_PORT"),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vpn-test',
        'USER': 'admin',
        'PASSWORD': '16zomole',
        'HOST': 'localhost',
        'PORT': 45047,
    }
}

# docker run -itd -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=16zomole -e POSTGRES_DB=vpn-test -p 45047:5432 --name vpn-test-pg postgres:13.3


IMAGE_NAME = "vpn-debian"
NUMBER_CONTAINERS = 10
VPN_PREFIX = "vpn_dion_server_"
LISTEN_PORT = 34078