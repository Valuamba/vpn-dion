import json
import logging
from typing import List

import requests

from helpers.dummy_data import WG_TEST_DATA
from lib.vpn_server.datatypes import VpnConfig, InstanceStatistic, WgInfoList, InstanceResponse, WgInfo

logger = logging.getLogger(__name__)


class VpnServerApiClient:

    def __init__(self, api_origin):
        self.api_origin = api_origin

    def collect_wg_connections(self) -> List[WgInfo]:
        logger.info(f'Collect Wireguard connections info')
        response = self.get(f'wg-connections')
        response.raise_for_status()
        json_data = json.loads(response.content)
        return WgInfoList.parse_raw(json_data['data']).__root__
        # instance_response = InstanceResponse.parse_raw(response.content)
        #
        # return instance_response.data.__root__

    def collect_statistics(self) -> InstanceStatistic:
        logger.info(f'Collect statistics')
        response = self.get(f'collect-statistics')
        response.raise_for_status()

        return InstanceStatistic.parse_raw(response.content)

    def create_client(self, user_id) -> VpnConfig:
        logger.info(f'Create client for user {user_id} and origin {self.api_origin}')
        response = self.get(f'addClient/{user_id}')
        response.raise_for_status()
        json_data = response.json()

        return VpnConfig.parse(json_data['data'])

    def remove_client(self, config_name):
        response = self.get(f'removeClient/{config_name}')
        response.raise_for_status()

    def post(self,  method_name: str, payload=None, data=None, files=None, params=None):
        target_url = f"{self.api_origin}{method_name}"

        logger.debug(
            f"Calling VPN Server API: method_name={method_name} payload={payload}"
        )

        response = requests.post(
            target_url, json=payload, files=files, params=params, data=data, timeout=10
        )

        try:
            logger.debug(
                f"Response: status={response.status_code} data={response.json()}"
            )
        except Exception as e:
            logger.exception(e)

        try:
            response.raise_for_status()
        except Exception as e:
            logger.exception(e)

        return response

    def get(self, method_name: str, params=None):
        target_url = f"{self.api_origin}{method_name}"

        logger.debug(
            f"Calling VPN Server API: method_name={method_name}"
        )

        response = requests.get(target_url, params=params, timeout=10)

        try:
            logger.debug(
                f"Response: status={response.status_code} data={response.json()}"
            )
        except Exception as e:
            logger.exception(e)

        try:
            response.raise_for_status()
        except Exception as e:
            logger.exception(e)

        return response

