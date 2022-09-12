from hashlib import md5

from django.conf import settings


def get_freekassa_checkout(
        *,
        amount: int,
        currency: str,
        subscription_id: int,
        **kwargs
):
    freekassa_origin = 'https://pay.freekassa.ru/'

    secret = md5(f'{settings.FREE_KASSA_MERCHANT_ID}:{amount}:{settings.FREE_KASSA_SECRET}:{currency}:{subscription_id}'.encode('utf-8')).hexdigest()

    params = {
        'm': settings.FREE_KASSA_MERCHANT_ID,
        'oa': amount,
        'currency': currency,
        'o': subscription_id,
        's': secret,
        **kwargs
    }

    param_line = '&'.join([ f'{key}={value}' for key, value in params.items()])

    return f'{freekassa_origin}?{param_line}'