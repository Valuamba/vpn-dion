import enum


class Options(enum.IntEnum):
    AddNewUser = 1
    RevokeExistingUser = 2
    UninstallWireGuard = 3
    Exit = 4


class ClientConfigDto:
    private_key: str
    address: str
    dbs: str

    public_key: str
    preshared_key: str
    endpoint: str
    allowed_ips: str