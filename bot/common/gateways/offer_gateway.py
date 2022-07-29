from typing import List

from aiohttp import ClientSession

from common.models.protocol import Protocol
from common.models.subscription_offer import SubscriptionOffer, SubscriptionDurationOffer, SubscriptionDeviceOffer, \
    SubscriptionOfferDevicesType


# async def get_subscription_offers() -> List[SubscriptionOffer]:
#     offers: List[SubscriptionOffer] = [
#         SubscriptionOffer(pkid=1, month_duration=1, devices_count=1, discount_percentage=0),
#         SubscriptionOffer(pkid=2, month_duration=1, devices_count=2, discount_percentage=15),
#         SubscriptionOffer(pkid=3, month_duration=1, devices_count=3, discount_percentage=20),
#         SubscriptionOffer(pkid=4, month_duration=1, devices_count=4, discount_percentage=30),
#
#         SubscriptionOffer(pkid=5, month_duration=6, devices_count=1, discount_percentage=0),
#         SubscriptionOffer(pkid=6, month_duration=6, devices_count=2, discount_percentage=20),
#         SubscriptionOffer(pkid=7, month_duration=6, devices_count=3, discount_percentage=25),
#         SubscriptionOffer(pkid=8, month_duration=6, devices_count=4, discount_percentage=35),
#
#         SubscriptionOffer(pkid=9, month_duration=12, devices_count=1, discount_percentage=0),
#         SubscriptionOffer(pkid=10, month_duration=12, devices_count=2, discount_percentage=25),
#         SubscriptionOffer(pkid=11, month_duration=12, devices_count=3, discount_percentage=30),
#         SubscriptionOffer(pkid=12, month_duration=12, devices_count=4, discount_percentage=50),
#     ]
#     return offers
#

async def get_subscription_offers() -> List[SubscriptionDurationOffer]:
    offers: List[SubscriptionDurationOffer] = [
        SubscriptionDurationOffer(pkid=1, month_duration=1, device_offers=get_devices_count(0, 15, 20, 30)),
        SubscriptionDurationOffer(pkid=2, month_duration=6, device_offers=get_devices_count(0, 20, 25, 35)),
        SubscriptionDurationOffer(pkid=3, month_duration=12, device_offers=get_devices_count(0, 25, 30, 50)),
    ]
    return offers


def get_devices_count(one_perc, two_perc, three_perc, four_perc) -> []:
    devices = [
        SubscriptionDeviceOffer(pkid=1, device_type=SubscriptionOfferDevicesType.ONE, discount_percentage=one_perc),
        SubscriptionDeviceOffer(pkid=2, device_type=SubscriptionOfferDevicesType.TWO, discount_percentage=two_perc),
        SubscriptionDeviceOffer(pkid=3, device_type=SubscriptionOfferDevicesType.THREE, discount_percentage=three_perc),
        SubscriptionDeviceOffer(pkid=4, device_type=SubscriptionOfferDevicesType.FOUR_OR_MORE, discount_percentage=four_perc)
    ]
    return devices


# def get_offers(aiohttp: ClientSession):
#     async with aiohttp.get(f'http://127.0.0.1:8000/api/rent/daily/get/{adv_id}') as response:
#         if response.status == 200:
#             return json.loads(await response.text())
#         else:
#             return None

def get_protocols():
    return [
        Protocol(pkid=1, name='Wireguard'),
        Protocol(pkid=2, name='OpenVPN'),
    ]