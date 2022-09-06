import os.path
from pathlib import Path
from typing import NamedTuple

from environs import Env


class Config(NamedTuple):
    __env = Env()
    __env.read_env(os.path.join(os.getcwd(), '../.env'))

    BASE_DIR = Path(__name__).resolve().parent.parent

    BOT_TOKEN = __env.str('BOT_TOKEN')

    VPN_REST = __env.str('VPN_REST')
    VPN_REST_HTTPS = __env.str('VPN_REST_HTTPS')
    VPN_BEARER_TOKEN = __env.str('VPN_BEARER_TOKEN')
    WEB_APP_SUBSCRIBE_LINK = __env.str('WEB_APP_LINK') + '?state=MakeAnOrder'

    MONGODB_DATABASE = __env.str('MONGODB_DATABASE')
    MONGODB_USERNAME = __env.str('MONGODB_USERNAME')
    MONGODB_PASSWORD = __env.str('MONGODB_PASSWORD')
    MONGODB_HOSTNAME = __env.str('MONGODB_HOSTNAME')
    MONGODB_PORT = __env.str('MONGODB_PORT')
    MONGODB_URI = 'mongodb://'

    YOOMONEY_PROVIDER_TOKEN = __env.str('YOOMONEY_PROVIDER_TOKEN')

    LOG_FILE_PATH = os.path.join(os.getcwd(), 'logs/log.log')

    if MONGODB_USERNAME and MONGODB_PASSWORD:
        MONGODB_URI += f"{MONGODB_USERNAME}:{MONGODB_PASSWORD}@"
    MONGODB_URI += f"{MONGODB_HOSTNAME}:{MONGODB_PORT}"