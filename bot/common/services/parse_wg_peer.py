"""
peer: Iw4mZ1kjF48I9NaEwzc5kP440M0YvglWKpL9M/+CVEA=
  preshared key: (hidden)
  endpoint: 92.255.165.72:60290
  allowed ips: 10.66.66.3/32, fd42:42:42::3/128
  latest handshake: 3 days, 3 hours, 14 minutes, 21 seconds ago
  transfer: 30.78 MiB received, 467.93 MiB sent

peer: dTKCw/mjM+YSF0bdYBrLyusalxu1Tv/7j9mZL7f9IEs=
  preshared key: (hidden)
  allowed ips: (none)
"""
import re

with open('./wg-conn.txt') as f:
    content = f.read()
    match = re.match('(peer:)(.*\n..)(.*\n..)(.*\n..)(.*\n..)(.*\n..)(.*\n)', content)
    match2 = re.findall('((peer:)(.*\n..){1,5}(.*\n))', content)
    match3 = re.findall('(peer:(.*\n..){1,5}.*\n)', content)

    peers = content.split('peer')

    for peer in peers:
        preshared_key = re.match('((?<=preshared key: )(.*))', peer).group()
        if len(preshared_key) > 0:
            s = preshared_key.group()[0]
        endpoint = re.search('(?<=endpoint: )(.*)', peer)
        allowed_ips = re.search('(?<=allowed ips: )(.*)', peer)
        latest_handshake = ('(?<=latest handshake: )(.*)', peer)
        transfer = re.search('(?<=transfer: )(.*)', peer)

        pass

    r = re.compile("(peer:(.*\n..){1,5}.*\n)")
    m = r.findall(content)

    m2 = re.search(r'(peer:(.*\n..){1,5}.*\n)', content)
    if match:
        print(content[match.start():match.end()])

    matches = re.findall('(peer:(.*\n..){1,5}.*\n)', content, re.DOTALL)
    print(matches)

    for m in match2:
        s = m.__str__
        print (s)

    pass
