import json

from django.shortcuts import render
import pymorphy2


# Create your views here.
from apps.vpn_subscription.models import VpnSubscription


def get_morph(text, count):
    morph = pymorphy2.MorphAnalyzer()
    text_morph = morph.parse(text)[0]
    text_morph.inflect({'gent'})
    return text_morph.make_agree_with_number(count).word


def get_payment_checkout(request):
    subscription_id = request.GET['subscription_id']
    payment_provider = request.GET['payment_provider']

    subscription: VpnSubscription = VpnSubscription.objects.get(pkid=subscription_id)

    payment_url = None
    if payment_provider == 'freekassa':
        payment_url = 'https://pay.freekassa.ru/?m=20336&oa=1000&currency=RUB&o=1&s=43400336c7d3daa74b3adbdfe46e94f0'

    month_duration = subscription.tariff_data.duration_data.month_duration
    devices_number = subscription.tariff_data.devices_number

    sub_data = {
        'duration': month_duration,
        'duration_loc': get_morph('месяц', month_duration),
        'devices_number': devices_number,
        'devices_loc': get_morph('устройство', devices_number),
        'price': subscription.tariff_data.discounted_price(),
        'currency': 'RUB',
        'discount': subscription.tariff_data.discount_percentage
    }

    return render(request, 'payment/payment_processing.html', {
        'subscription': json.dumps(sub_data),
        'payment_provider': payment_url
    })