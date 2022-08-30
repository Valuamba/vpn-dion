from typing import List

from common.models.instnace import Instance


async def get_available_instances() -> List[Instance]:
    return [
        Instance(pkid=1, ip_address='192.168.8.12', is_online=True, country='Belarus', discount=0),
        Instance(pkid=2, ip_address='192.168.8.12', is_online=True, country='Russia', discount=0),
        Instance(pkid=3, ip_address='192.168.8.12', is_online=True, country='Germany', discount=0),
        Instance(pkid=4, ip_address='192.168.8.12', is_online=True, country='USA', discount=20),
        Instance(pkid=5, ip_address='192.168.8.12', is_online=True, country='Niderlands', discount=0),
    ]