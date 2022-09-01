import json
import logging
import traceback
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.utils import timezone
from djmoney.money import Money
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_instance.models import VpnInstance
from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus, VpnPaymentTransaction, \
    SubReminderState
from apps.vpn_subscription.serializers import CreateSubscriptionConfigsRequest
from lib.freekassa import get_freekassa_checkout
from lib.mock import get_mock_vpn_config
from lib.morph import get_morph
from lib.vpn_server.datatypes import VpnConfig
import hmac
import hashlib

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_subscription_checkout(request, subscription_id):
    logger.info(f'Getting subscription {subscription_id}.')

    try:
        subscription = VpnSubscription.objects.get(pkid=subscription_id)
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': f'Subscription {subscription_id} was not found'}, status=status.HTTP_404_NOT_FOUND)

    freekassa_url = get_freekassa_checkout(subscription.price.amount, "RUB", subscription.pkid)

    return Response(data={
        'month_duration': subscription.month_duration,
        'month_loc': get_morph('месяц', subscription.month_duration),
        'devices_number': subscription.devices_number,
        'devices_loc': get_morph('устройство', subscription.devices_number),
        'price': subscription.price.amount,
        'currency': subscription.price.currency.code,
        'discount': subscription.discount,
        'subscription_id': subscription.pkid,
        'freekassa_url': freekassa_url
    })


@api_view(['POST'])
def calculate_invoice(request):
    data = request.data
    tariff_id = data['tariff_id']
    devices = json.loads(data['devices'])

    logger.info(f'Calcaulate invoice for tariff {tariff_id} and {len(devices)} amount of devices')

    tariff = VpnDeviceTariff.objects.get(pkid=tariff_id)

    return Response(data={
        'discount': tariff.total_discount,
        'price': tariff.discounted_price(devices)
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@transaction.atomic
def create_subscription(request):
    data = request.data
    user_id = data['user_id']
    tariff_id = data['tariff_id']
    devices = json.loads(data['devices'])

    logger.info(f'Create subscription for tariff {tariff_id} and user {user_id}.')

    # settings.BOT_TOKEN
    #
    # data_check_string = ...
    # secret_key = HMAC_SHA256(settings.BOT_TOKEN, "WebAppData")
    # if (hex(HMAC_SHA256(data_check_string, secret_key)) == hash):
    #     pass
    #
    # signature = hmac.new(
    #     str(API_SECRET),
    #     msg=message,
    #     digestmod=hashlib.sha256
    # ).hexdigest().upper()

    # CreateSubscriptionSerilizer(data=data).is_valid(True)

    tariff = VpnDeviceTariff.objects.get(pkid=tariff_id)

    total_price = tariff.discounted_price(devices)
    total_discount = tariff.total_discount

    with transaction.atomic():
        subscription = VpnSubscription.objects.create(
            user_id=user_id,
            tariff_id=tariff_id,
            month_duration=tariff.duration.month_duration,
            devices_number=tariff.devices_number,
            is_referral=False,
            price=Money(amount=total_price, currency="RUB"),
            discount=total_discount,
            subscription_end=datetime.today() + relativedelta(months=tariff.duration.month_duration),
            status=SubscriptionPaymentStatus.WAITING_FOR_PAYMENT,
            reminder_state=SubReminderState.SEVEN_DAYS_REMINDER
        )

        for device in devices:
            instances = VpnInstance.objects.filter(country__pkid=device['country_id'],
                                                   protocols__pkid=device['protocol_id'], is_online=True
                                                   )
            if len(instances) == 0:
                return Response(data={'detailed: There are no instances'}, status=status.HTTP_404_NOT_FOUND)

            VpnItem.objects.create(instance=instances[0], protocol_id=device['protocol_id'],
                vpn_subscription_id=subscription.pkid
            )

        freekassa_url = get_freekassa_checkout(total_price, "RUB", subscription.pkid)
        return Response(data=freekassa_url, status=status.HTTP_200_OK)


@api_view(['POST'])
@transaction.atomic
def successful_subscription_extension(request):
    try:
        data = request.data
        email = data["P_EMAIL"]
        phone = data["P_PHONE"]
        sign = data["SIGN"]
        amount = data['AMOUNT']
        currency_id = data['CUR_ID']
        subscription_id = data['MERCHANT_ORDER_ID']

        logger.info(f'Create successful extension subscription {subscription_id} payment transaction.')

        try:
            subscription = VpnSubscription.objects.get(pkid=subscription_id)
        except VpnSubscription.DoesNotExist:
            return Response(data={'details': f'Subscription {subscription_id} was not found'}, status=status.HTTP_404_NOT_FOUND)

        if subscription.subscription_end < datetime.now():
            return Response(data={'details': f'Subscription {subscription_id} is outdated.'}, status=status.HTTP_404_NOT_FOUND)

        if subscription.is_referral:
            return Response(data={'details': f'Subscription {subscription_id} with referral type cannot be extended.'}, status=status.HTTP_404_NOT_FOUND)

        if subscription.status != SubscriptionPaymentStatus.PAID_SUCCESSFULLY:
            return Response(data={'details': f'Subscription {subscription_id} has wrong status for extension.'}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            payment_transaction = VpnPaymentTransaction.objects.create(
                email=email,
                sign=sign,
                phone=phone,
                currency_id=currency_id,
                price=amount,
                subscription_id=subscription_id
            )

            subscription.subscription_end = subscription.subscription_end + relativedelta(months=subscription.month_duration)
            subscription.save()

            return Response(status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')
        return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@transaction.atomic
def successful_payment(request):
    data = request.data
    email = data["P_EMAIL"]
    phone = data["P_PHONE"]
    sign = data["SIGN"]
    amount = data['AMOUNT']
    currency_id = data['CUR_ID']
    subscription_id = data['MERCHANT_ORDER_ID']

    logger.info(f'Create successful extension subscription {subscription_id} payment transaction.')

    try:
        subscription = VpnSubscription.objects.get(pkid=subscription_id)
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': 'Subscription was not found'}, status=status.HTTP_404_NOT_FOUND)

    if subscription.status != SubscriptionPaymentStatus.WAITING_FOR_PAYMENT:
        return Response(data={'details': 'Subscription has wrong status'}, status=status.HTTP_404_NOT_FOUND)

    changed_items = []
    try:
        with transaction.atomic():
            payment_transaction = VpnPaymentTransaction.objects.create(
                email=email,
                sign=sign,
                phone=phone,
                currency_id=currency_id,
                price=amount,
                subscription_id=subscription_id
            )

            subscription.status = SubscriptionPaymentStatus.PAID_SUCCESSFULLY
            subscription.save()
            vpn_items = subscription.vpn_items_list

            for item in vpn_items:
                logger.info(f'Create config for vpn item {item.pkid}')
                client_response: VpnConfig = item.instance.client.create_client(subscription.user.user_id)
                item.public_key = client_response.public_key
                item.private_key = client_response.private_key
                item.address = client_response.address
                item.dns = client_response.dns
                item.preshared_key = client_response.preshared_key
                item.endpoint = client_response.endpoint
                item.allowed_ips = client_response.allowed_ips
                item.config_name = client_response.config_name
                item.save()
                changed_items.append(item)
    except Exception as e:
        for item in changed_items:
            item.instance.client.remove_client(item.config_name)
        logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')
        return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.atomic
def fail_subscription(request, subscription_id):
    logger.info(f'Fail subscription {subscription_id}.')
    try:
        subscription = VpnSubscription.objects.get(pkid=subscription_id)
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': 'Subscription was not found'}, status=status.HTTP_404_NOT_FOUND)
    subscription.status = SubscriptionPaymentStatus.PAYMENT_WAS_FAILED
    subscription.save()

    for item in subscription.vpn_items_list:
        item.instance.client.remove_client(item.config_name)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def list_user_subscriptions(request, user_id):
    logger.info(f'List user {user_id} subscriptions.')
    try:
        subscriptions = VpnSubscription.objects.filter(user_id=user_id, status__in=[SubscriptionPaymentStatus.PAID_SUCCESSFULLY])
            # .values('user', 'tariff', )
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': 'Subscription was not found'}, status=status.HTTP_404_NOT_FOUND)

    data = []
    for sub in subscriptions:
        data.append({
            'month_duration': sub.month_duration,
            'days_duration': sub.days_duration,
            'is_referral': sub.is_referral,
            'devices_number': sub.devices_number,
            'subscription_id': sub.pkid
        })

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def activate_invited_user_trial_subscription(request):
    days_duration = request.data.get('days_duration')
    user_id = request.data.get('user_id')

    logger.info(f'Activate free subscription with {days_duration} days for invited user {user_id}')

    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    devices_number = 1
    country = VpnCountry.get_defaults()[0]
    protocol = VpnProtocol.get_defaults()[0]
    subscription_end = timezone.now() + relativedelta(days=days_duration)

    if not country:
        return Response(data={'detailed: Country was not found.'}, status=status.HTTP_404_NOT_FOUND)

    if not protocol:
        return Response(data={'detailed: Protocol was not found.'}, status=status.HTTP_404_NOT_FOUND)

    changed_items = []
    subscription_id = None
    try:
        with transaction.atomic():
            subscription = VpnSubscription.objects.create(user_id=user_id,
                                                          status=SubscriptionPaymentStatus.PAID_SUCCESSFULLY,
                                                          devices_number=1,
                                                          days_duration=7,
                                                          subscription_end=subscription_end,
                                                          is_referral=True,
                                                          reminder_state=SubReminderState.SEVEN_DAYS_REMINDER
                                                          )
            subscription_id = subscription.pkid
            changed_items = create_vpn_items(country, protocol, devices_number, subscription.pkid, user_id)
    except Exception as e:
        for item in changed_items:
            item.instance.client.remove_client(item.config_name)
        logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')
        return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={
        'subscription_id': subscription_id
    },
        status=status.HTTP_200_OK
    )


def create_vpn_items(country, protocol, devices_number, subscription_id, user_id):
    changed_items = []
    for i in range(devices_number):
        instance = VpnInstance.objects.filter(country=country, protocols=protocol, is_online=True).first()
        if not instance:
            raise Exception('There are no instances')

        # client_response: VpnConfig = get_mock_vpn_config()
        client_response = instance.client.create_client(user_id)

        item = VpnItem(instance=instance, protocol=protocol, vpn_subscription_id=subscription_id)
        logger.info(f'Create config for vpn item {item.pkid}')
        item.public_key = client_response.public_key
        item.private_key = client_response.private_key
        item.address = client_response.address
        item.dns = client_response.dns
        item.preshared_key = client_response.preshared_key
        item.endpoint = client_response.endpoint
        item.allowed_ips = client_response.allowed_ips
        item.config_name = client_response.config_name
        item.save()
        changed_items.append(item)

    return changed_items

@api_view(['POST'])
@transaction.atomic
def activate_referral_subscription(request):
    month_duration = request.data.get('month_duration', 0)
    days_duration = request.data.get('days_duration', 0)
    user_id = request.data.get('user_id')

    logger.info(f'Create referral subcsription {month_duration} month {days_duration} days for user {user_id}')

    if (not month_duration and not days_duration) or (month_duration == 0 and days_duration == 0):
        return Response(data={'detailed: Wrong duration parameters.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    free_referrals = user.free_referrals_data

    if len(free_referrals) == 0:
        return Response(data={'details': 'There is no referrals with is_activated_reward=False'}, status=status.HTTP_400_BAD_REQUEST)

    devices_number = 1
    month_duration = len(free_referrals)
    country = VpnCountry.get_defaults()[0]
    protocol = VpnProtocol.get_defaults()[0]
    subscription_end = timezone.now() + relativedelta(months=month_duration, days=days_duration)

    if not country:
        return Response(data={'detailed: Country was not found.'}, status=status.HTTP_404_NOT_FOUND)

    if not protocol:
        return Response(data={'detailed: Protocol was not found.'}, status=status.HTTP_404_NOT_FOUND)

    changed_items = []
    subscription_id = None
    try:
        with transaction.atomic():
            for referral in free_referrals:
                referral.is_activated_reward = True
                referral.save()

            subscription = VpnSubscription.objects.create(user_id=user_id,
                                                          month_duration=month_duration,
                                                          devices_number=devices_number,
                                                          discount=0,
                                                          status=SubscriptionPaymentStatus.PAID_SUCCESSFULLY,
                                                          subscription_end=subscription_end,
                                                          is_referral=True,
                                                          reminder_state=SubReminderState.SEVEN_DAYS_REMINDER)
            subscription_id = subscription.pkid
            changed_items = create_vpn_items(country, protocol, devices_number, subscription.pkid, user_id)
    except Exception as e:
        for item in changed_items:
            item.instance.client.remove_client(item.config_name)
        logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')
        return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={
        'devices_number': devices_number,
        'month_duration': month_duration,
        'subscription_id': subscription_id
    },
        status=status.HTTP_200_OK)