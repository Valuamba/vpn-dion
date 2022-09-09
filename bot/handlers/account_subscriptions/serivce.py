import os
import re
from urllib.parse import urljoin

from aiogram.types import InputMediaPhoto, FSInputFile

from common.services.vpn_client_webapi import send_get, send_get_content, gettext
from config import Config
from utils.update import get_chat_id


async def get_all_user_subscriptions(user_id, vpn_client):
    response = await send_get(vpn_client, f'subscription/user-subscriptions/{user_id}/')
    user_subscriptions = response.parsed
    return user_subscriptions


async def get_all_subscription_devices(subscription_id, vpn_client):
    response = await send_get(vpn_client, f'vpn-item/list_with_subscription/{subscription_id}')
    subscription_devices = response.parsed
    return subscription_devices


async def get_config_vpn(device_id, vpn_client):
    response = await send_get_content(vpn_client, f'vpn-item/config/{device_id}/')
    return response.content


async def get_device_vpn_settings(device_id, vpn_client):
    response = await send_get(vpn_client, f'vpn-item/{device_id}/')
    vpn_item = response.parsed
    return vpn_item


def get_device_qrcode(device_id):
    return urljoin(Config.VPN_REST_HTTPS, f'api/v1/vpn-item/qrcode/{device_id}/')


def absolute_file_pats(directory):
    for dirpath,_,filenames in os.walk(directory):
        sorted_files = sorted(filenames, key=lambda f: int(re.match('\d+(?<!.jpg)', f).group(0)), reverse=False)
        for file_name in sorted_files:
            yield os.path.abspath(os.path.join(dirpath, file_name))


async def send_tutorial(sub_directory, alias, bot, ctx):
    text = await gettext(alias)
    medias = [InputMediaPhoto(media=FSInputFile(path=m)) for m in
              absolute_file_pats(os.path.join(Config.ROOT_DIR, 'common/assets', sub_directory))]
    if len(medias) > 8:
        first_part = medias[:8]
        second_part = medias[8:]
        await bot.send_media_group(get_chat_id(ctx), media=first_part)
        await bot.send_media_group(get_chat_id(ctx), media=second_part)
    elif len(medias) > 0:
        await bot.send_media_group(get_chat_id(ctx), media=medias)
        await bot.send_message(get_chat_id(ctx), text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(get_chat_id(ctx), text=text, disable_web_page_preview=True)
