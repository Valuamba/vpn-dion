# from django.test import TestCase
# # from django.conf import settings
# # from lib.currency_converter import convert_currency
#
#
# class CurrencyConverterTestCase(TestCase):
#
#     # def test_check_wrong_currencies(self):
#     #     s = convert_currency('RUB', 'USD', '1000.00')
#
#     def test_check_some(self):
#
#         self.assertTrue(1==1)


import pytest
from lib.currency_converter import CurrencyConverterApiClient


def test_user_str():
    CURRENCY_CONVERTER_ORIGIN = "https://currency-converter5.p.rapidapi.com/currency/convert"
    RAPID_API_KEY = "8ad5cb8b5amshfeeb70fa11ca46ap19d693jsnab3ee023007d"
    RAPID_API_HOST = "currency-converter5.p.rapidapi.com"

    from_c='RUB'
    to_c='USD'
    amount='100.02'

    service = CurrencyConverterApiClient(CURRENCY_CONVERTER_ORIGIN, RAPID_API_KEY, RAPID_API_HOST).convert_currency(from_c, to_c, amount)

    assert service