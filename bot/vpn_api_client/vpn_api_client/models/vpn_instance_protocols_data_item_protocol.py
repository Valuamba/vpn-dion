from enum import Enum


class VpnInstanceProtocolsDataItemProtocol(str, Enum):
    WIREGUARD = "wireguard"
    OPEN_VPN = "open_vpn"

    def __str__(self) -> str:
        return str(self.value)
