import json
import logging
import traceback

from aiogram.client.session import aiohttp

logger = logging.getLogger(__name__)


class VpnRestClient:

    def __init__(self, api_origin, bearer_token):
        self.api_origin = api_origin
        self.bearer_token = bearer_token
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            'content-type': 'application/json'
        }
        # self.session = aiohttp.ClientSession()

    # async def __aenter__(self):
    #     self.session = await aiohttp.ClientSession(headers=self.headers).__aenter__()
    #     return self
    #
    # def __aexit__(self, exc_type, exc_value, tb):
    #     # if exc_type is not None:
    #     #     traceback.print_exception(exc_type, exc_value, tb)
    #     #     # return False # uncomment to pass exception through
    #     self.session.__aexit__(exc_type, exc_value, tb)

    async def add_subscription(self, subscription):
        return await self.post("subscription/addSubscription", data=subscription)

    async def get_available_protocols(self):
        return await self.get("bot_assets/active-protocols")

    async def get_available_countries(self):
        return await self.get("bot_assets/active-countries")

    async def get_tariffs(self):
        return await self.get('bot_assets/offers')

    async def get(self, method_name: str, payload=None, data=None):
        target_url = f"{self.api_origin}/{method_name}"

        logger.debug(
            f"Calling VPN Server API: method_name={method_name} payload={payload}"
        )
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(target_url, data=data) as response:
                try:
                    logger.debug(
                        f"Response: status={response.status} data={await response.json()}"
                    )
                except Exception as e:
                    logger.exception(e)

                try:
                    response.raise_for_status()
                except Exception as e:
                    logger.exception(e)

                return await response.json()

    async def post(self, method_name: str, payload=None, data=None):
        target_url = f"{self.api_origin}/{method_name}"

        logger.debug(
            f"Calling VPN Server API: method_name={method_name} payload={payload}"
        )

        json_data = json.dumps(data)

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(target_url, data=json_data) as response:
                try:
                    logger.debug(
                        f"Response: status={response.status} data={await response.json()}"
                    )
                except Exception as e:
                    logger.exception(e)

                try:
                    response.raise_for_status()
                except Exception as e:
                    logger.exception(e)

                return await response.json()