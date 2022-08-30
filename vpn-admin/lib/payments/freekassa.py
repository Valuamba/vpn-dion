import requests
import hashlib

api_origin = "https://api.freekassa.ru/v1/"

payment_origin = 'https://pay.freekassa.ru/'

# target_url = f"{api_origin}/{method_name}"

# response = requests.post(target_url,data={})


def get_payment_signature(merchant_id: int, price: float, secret: str, currency: str, order_id: int) -> str:
    signature_str = '%s:%s:%s:%s:%s' % (merchant_id, price, secret, currency, order_id)
    return hashlib.md5(signature_str.encode('utf-8')).hexdigest()


def get_payment_url(merchant_id: int, price: float, secret: str, currency: str, order_info):
    sign = get_payment_signature(merchant_id, price, secret, currency, order_info)

    text = []
    text.append(f'm={merchant_id}')
    text.append(f'oa={price}')
    text.append(f'currency={currency}')
    text.append(f'o={order_info}')
    text.append(f's={sign}')

    req_parameters = '?' + '&'.join(text)
    return payment_origin + req_parameters


print (get_payment_url(merchant_id=20336, price=1000, secret='Q/WRnd+TO^+JBQ,', currency='RUB', order_info='valuamba'))

