import uuid
from typing import List

from django.db.models import Q
from django.utils import timezone

from apps.promocode.models import PromoCode
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_device_tariff.selectors import calculate_discounted_price
from apps.vpn_instance.models import VpnInstance
from apps.vpn_item.models import VpnItem
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription


def get_default_country() -> VpnCountry:
    return VpnCountry.get_defaults()[0]


def get_default_protocol() -> VpnProtocol:
    query = Q(instances__is_online=True, is_default=True)
    protocols = VpnProtocol.objects.filter(query)
    return protocols[0]


def get_promo_code(promo_code: str) -> PromoCode:
    try:
        query = Q(promocode=promo_code)
        return PromoCode.objects.get(query)
    except PromoCode.DoesNotExist:
        return None


def get_subscription_by_uuid(id: uuid) -> VpnSubscription:
    return VpnSubscription.objects.get(id=id)


def get_subscription_by_id(*, id: int) -> VpnSubscription:
    return VpnSubscription.objects.get(pkid=id)

def get_subscription_vpn_items(*, subscription_id) -> List[VpnItem]:
    return VpnItem.objects.filter(vpn_subscription_id=subscription_id)

def get_available_countries() -> List[VpnCountry]:
    results = VpnCountry.objects.raw('''
        SELECT c.pkid, place, discount_percentage, is_default, locale_ru FROM public.vpn_countries as c 
        INNER JOIN public.vpn_instances as i on country_id = c.pkid
        WHERE i.is_online=True and c.is_default=True
        GROUP BY c.pkid, place, discount_percentage
        ''')
    return results


def get_available_protocols() -> List[VpnProtocol]:
    results = VpnProtocol.objects.raw('''
        SELECT p.pkid, p.protocol, p.is_default FROM public.vpn_protocols as p
        INNER JOIN public.vpn_instances_protocols ON vpn_instances_protocols.vpnprotocol_id = p.pkid 
        INNER JOIN public.vpn_instances vpn_instances2 ON vpn_instances2.pkid = vpn_instances_protocols.vpninstance_id
        WHERE vpn_instances2.is_online=True and p.is_default=True
        GROUP BY p.pkid, protocol
    ''')
    return results


# TODO добавить inner join
def get_promo_code_for_subscription(*, promo_code: str, user_id: int):
    try:
        promo_code_obj: PromoCode = PromoCode.objects.get(promo_code=promo_code, expires__gt=timezone.now())
    except PromoCode.DoesNotExist:
        return { 'is_promo_code_ready': False }

    user = next((user for user in promo_code_obj.applied_by_users.all() if user.user_id == int(user_id)), None)
    is_promo_code_ready = user is None

    return {
        'discount': promo_code_obj.discount,
        'name': promo_code_obj.name,
        'is_promo_code_ready': is_promo_code_ready
    }


def get_subscription_by_id(*, subscription_id: int) -> VpnSubscription:
    return VpnSubscription.objects.get(pkid=subscription_id)


def get_subscription_device_list(*, subscription_id: int) -> []:
    # logger.info(f'Get VPN Items of subscription {subscription_id}')
    vpn_items = VpnItem.objects.filter(vpn_subscription_id=subscription_id)

    data = []
    for vpn_item in vpn_items:
        data.append({
            'vpn_item_id': vpn_item.pkid,
            'country': vpn_item.instance.country.locale_ru,
            'protocol': vpn_item.protocol.protocol,
        }
        )
    return data


def get_vpn_config_file(request, vpn_item_id):
    # logger.info(f'Get VPN config {vpn_item_id}')
    vpn_item = VpnItem.objects.get(pkid=vpn_item_id)


def get_vpn_item(*, vpn_item_id) -> VpnItem:
    return VpnItem.objects.get(pkid=vpn_item_id)


def get_available_instance(*, country_id, protocol_id) -> VpnInstance:
    query = Q(country__pkid=country_id, protocols__pkid=protocol_id, is_online=True)
    instances = VpnInstance.objects.filter(query)

    if len(instances) == 0:
        raise Exception('There are no available instances.')

    return instances[0]


def get_one_device_tariffs() -> List[VpnDeviceTariff]:
    query = Q(devices_number=1)
    return VpnDeviceTariff.objects.filter(query).order_by('duration__month_duration')


def get_outdated_subscription_configs() -> List[VpnItem]:
    subscriptions: List[VpnSubscription] = VpnSubscription.objects.filter(subscription_end__lt=timezone.now())
    
    vpn_items: List[VpnItem] = []
    
    for sub in subscriptions:
        for vpn_item in sub.vpn_items_list:
            vpn_items.append(vpn_item)
      
    return vpn_items