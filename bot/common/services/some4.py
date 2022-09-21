import subprocess
import re
from typing import Optional

from pydantic import BaseModel

# content = """
# peer: Iw4mZ1kjF48I9NaEwzc5kP440M0YvglWKpL9M/+CVEA=
#   preshared key: (hidden)
#   endpoint: 92.255.165.72:60290
#   allowed ips: 10.66.66.3/32, fd42:42:42::3/128
#   latest handshake: 3 days, 3 hours, 14 minutes, 21 seconds ago
#   transfer: 30.78 MiB received, 467.93 MiB sent
#
# peer: dTKCw/mjM+YSF0bdYBrLyusalxu1Tv/7j9mZL7f9IEs=
#   preshared key: (hidden)
#   allowed ips: (none)
# """

p = subprocess.Popen('wg show', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
out = out.decode('utf-8')
err = err.decode('utf-8')


class WgInfo(BaseModel):
    peer: Optional[str]
    preshared_key: Optional[str]
    endpoint: Optional[str]
    allowed_ips: Optional[str]
    latest_handshake: Optional[str]
    transfer: Optional[str]


r = re.compile('(?P<key>([a-z]+(\s?))*):\s*(?:"([^"]*)"|(?P<value>.*))')
matches = [m.groupdict() for m in r.finditer(out)]

wg_key_value = dict()
key_value_indexes = [idx for idx, match in enumerate(matches) if match['key'] == 'peer']


def create_wg_info(key_value_pairs) -> WgInfo:
    wg_info = WgInfo()
    for pair in key_value_pairs:
        setattr(wg_info, pair['key'].replace(' ', '_'), pair['value'])
    return wg_info


key_value_pair_list = []
for idx, key_index in enumerate(key_value_indexes):
    if idx == len(key_value_indexes) - 1:
        key_value_pair_list.append(create_wg_info(matches[key_index:]))
    else:
        key_value_pair_list.append(create_wg_info(matches[key_index: key_value_indexes[idx + 1]]))


for k in key_value_pair_list:
    print(k)
# print(f'List count: {len(key_value_pair_list)}')
