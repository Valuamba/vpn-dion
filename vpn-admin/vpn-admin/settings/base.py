import os
from datetime import timedelta
from pathlib import Path
import logging.config
from django.utils.log import DEFAULT_LOGGING
import environ

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent.parent

print (f'BASE DIR: {BASE_DIR}')
environ.Env.read_env(BASE_DIR / "../.env")
SECRET_KEY = env("SECRET_KEY")
SENTRY_DSN = env("SENTRY_DSN")
DEBUG = env("DEBUG")

# ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")
# ALLOWED_HOSTS = ['*']

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
#
# sentry_sdk.init(
#     dsn=SENTRY_DSN,
#     integrations=[
#         DjangoIntegration(),
#     ],
#     traces_sample_rate=1.0,
#     send_default_pii=True
# )

# CORS_ALLOW_ALL_ORIGINS = True


# CORS_ORIGIN_ALLOW_ALL = True
# # CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ORIGIN_WHITELIST = ()
# CORS_ALLOWED_ORIGINS = [
#     "https://domain.com",
# ]
    # CSRF_TRUSTED_ORIGINS = ['http://localhost:8080',
#                         "http://127.0.0.1:5000",
#                         "http://webapp",
#                         "]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT"
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(weeks=300),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'SIGNING_KEY': env("SIGNING_KEY"),
    'AUTH_HEADER_NAME': "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken", )
}

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    'djmoney',
    "rest_framework_simplejwt",
    'corsheaders',
    'emoji_picker',
]

LOCAL_APPS = ['apps.common',
              'apps.bot',
              'apps.vpn_configuration',
              'apps.vpn_tariffs',
              'apps.notifications', 'apps.vpn_order']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    # 'django.middleware.security.SecurityM',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vpn-admin.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'vpn-admin/templates'),
            os.path.join(BASE_DIR, 'apps/feedback/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vpn-admin.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# STATICFILES_DIRS = [
#     BASE_DIR / "staticfiles"
# ]


STATIC_URL = "/staticfiles/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIR = []
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = BASE_DIR / "mediafiles"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

log_path = os.path.join(BASE_DIR, 'logs')
isExist = os.path.exists(log_path)
if not isExist:
    os.makedirs(log_path)

# open(os.path.join(log_path, 'vpn-dion.log'), mode='a').close()

logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

SYNC_VPN_SERVER_INTERVAL_SECS=30

from logging.handlers import TimedRotatingFileHandler
logname = "my_app.log"
handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
handler.suffix = "%Y%m%d"
logger.addHandler(handler)

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
        },
        "file": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
        },
        "django.server": DEFAULT_LOGGING["formatters"]["django.server"]
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console"
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "file",
            "filename": os.path.join(BASE_DIR, "logs/vpn-dion.log"),
            'when': 'midnight',
            'backupCount': 10,
        },
        "django.server": DEFAULT_LOGGING["handlers"]["django.server"]
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": [
                "console",
                "file"
            ],
            "propagate": False
        },
        "apps": {
            "level": "INFO",
            "handlers": [
                "console"
            ],
            "propagate": False
        },
        "django.server": DEFAULT_LOGGING["loggers"]["django.server"]
    }
})


CURRENCY_CONVERTER_ORIGIN="https://currency-converter5.p.rapidapi.com/currency/convert"
RAPID_API_KEY="8ad5cb8b5amshfeeb70fa11ca46ap19d693jsnab3ee023007d"
RAPID_API_HOST="currency-converter5.p.rapidapi.com"

BOT_LOCALES_PATH=os.path.join(BASE_DIR.parent, 'assets/bot_locales.json')
BOT_USER_NAME=env.get_value('BOT_USER_NAME')
BOT_TOKEN=env.get_value('BOT_TOKEN')

FREE_KASSA_MERCHANT_ID=env.get_value('FREE_KASSA_MERCHANT_ID')
FREE_KASSA_SECRET=env.get_value('FREE_KASSA_SECRET')

TELEGRAM_API_ORIGIN = os.getenv("TELEGRAM_API_ORIGIN") or "https://api.telegram.org"

WEB_APP_LINK=os.getenv("WEB_APP_LINK")