from dataclasses import dataclass


@dataclass
class VpnConfig:
    private_key: str
    address: str
    dns: str
    public_key: str
    preshared_key: str
    endpoint: str
    allowed_ips: str
    config_name: str

    @classmethod
    def parse(cls, json_data) -> "VpnConfig":
        return cls(
            private_key=json_data.get("private_key"),
            endpoint=json_data.get("endpoint"),
            public_key=json_data.get("public_key"),
            address=json_data.get("address"),
            allowed_ips=json_data.get("allowed_ips"),
            preshared_key=json_data.get("preshared_key"),
            dns=json_data.get("dns"),
            config_name=json_data.get("config_name"),
        )
