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

import ddtrace
ddtrace.patch(logging=True)

API_LOG_APPLICATION_LEVEL="INFO"
API_LOG_STATE_LEVEL="INFO"
API_LOG_REQUEST_LEVEL="INFO"
API_LOG_SESSION_LEVEL="INFO"
API_LOG_ERROR_LEVEL="INFO"
API_LOG_ROOT = env.str("API_LOG_ROOT")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "{levelname} {message}", "style": "{"},
        "json": {"()": "django_datadog_logger.formatters.datadog.DataDogJSONFormatter"},
    },
    "handlers": {
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "console"},
        "socket_handler": {
           "level": API_LOG_ERROR_LEVEL,
           "class": "logging.handlers.SocketHandler",
           "host": "127.0.0.1",
           "port": 5559,
           "formatter": "json"
        },
        'logstash': {
            'level': 'INFO',
            'class': 'logstash.TCPLogstashHandler',
            'host': '127.0.0.1',   # IP/name of our Logstash EC2 instance
            'port': 5559,
            'version': 1,
            'message_type': 'logstash',
            'fqdn': True,
            'tags': ['myapp'],
            # "formatter": "json",
        }  
    },
    "loggers": {
        "": {"handlers": ["console", "logstash"], "level": "DEBUG", "propagate": True},
        "ddtrace": {"handlers": ["console", "logstash"], "level": "ERROR", "propagate": False},
        "django.db.backends": {"handlers": ["console", "logstash"], "level": "ERROR", "propagate": False},
        "twilio": {"handlers": ["console", "logstash"], "level": "ERROR", "propagate": False},
        "my_project": {"handlers": ["console", "logstash"], "level": "INFO", "propagate": False},
        "my_project.throttling": {"handlers": ["console", "logstash"], "level": "DEBUG", "propagate": False},
        "my_project.vehicles.viewsets.state": {"handlers": ["console", "logstash"], "level": "INFO", "propagate": False},
        "my_project.accounts.session": {"handlers": ["console", "logstash"], "level": "DEBUG", "propagate": False},
        "my_project.session": {"handlers": ["console", "logstash"], "level": "DEBUG", "propagate": False},
        "django_auth_ldap": {"level": "DEBUG", "handlers": ["console", "logstash"], "propagate": False},
        "django_datadog_logger.middleware.error_log": {"handlers": ["console", "logstash"], "level": "INFO", "propagate": False},
        "django_datadog_logger.middleware.request_log": {"handlers": ["console", "logstash"], "level": "INFO", "propagate": False},
        "django_datadog_logger.rest_framework": {"handlers": ["console", "logstash"], "level": "INFO", "propagate": False},
    },
}
DJANGO_DATADOG_LOGGER_EXTRA_INCLUDE = r"^(django_datadog_logger|my_project)(|\..+)$"

# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = "Europe/Moscow"