import json
from dataclasses import dataclass
from typing import List


@dataclass
class DeviceTariff:
    country_id: int
    protocol_id: int

    @classmethod
    def parse(cls, json_data) -> "DeviceTariff":
        return cls(
            country_id=json_data.get("country_id"),
            protocol_id=json_data.get("protocol_id")
        )


@dataclass
class PaymentTariff:
    tariff_id: int
    devices: List[DeviceTariff]

    @classmethod
    def parse(cls, json_data) -> "PaymentTariff":
        return cls(
            tariff_id=json_data.get("tariff_id"),
            devices=[DeviceTariff.parse(d) for d in json.loads(json_data.get("devices"))]
        )
