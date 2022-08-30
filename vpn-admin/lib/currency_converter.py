import requests
from django.conf import settings


def convert_currency(from_c: str, to_c: str, amount: str):
	headers = {
		"X-RapidAPI-Key": settings.RAPID_API_KEY,
		"X-RapidAPI-Host": settings.RAPID_API_HOST
	}
	querystring = {"format": "json", "from": from_c, "to": to_c, "amount": amount}
	response = requests.request("GET", settings.CURRENCY_CONVERTER_ORIGIN, headers=headers, params=querystring)

	return response.text


class CurrencyConverterApiClient:

	def __init__(self, origin, rapid_api, rapid_host):
		self.origin = origin
		self.headers = {
			"X-RapidAPI-Key": rapid_api,
			"X-RapidAPI-Host": rapid_host
		}

	def convert_currency(self, from_c: str, to_c: str, amount: str):
		querystring = {"format": "json", "from": from_c, "to": to_c, "amount": amount}
		response = requests.request("GET", self.origin, headers=self.headers, params=querystring)

		return response.text

