import subprocess

from pydantic import BaseModel

p = subprocess.Popen('ls -a', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
out = out.decode('utf-8')
err = err.decode('utf-8')

content = """
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


class WgInfo(BaseModel):
    peer: str
    preshared_key: str
    endpoint: str
    allowed_ips: str
    latest_handshake: str
    transfer: str


# matches = re.findall('(peer:(.*\n..){1,5}.*\n)', content)
matches = re.findall('(?P<key>([a-z]+(\s?))*):\s*(?:"([^"]*)"|(?P<value>.*))', content)
matches = re.finditer('(?P<key>([a-z]+(\s?))*):\s*(?:"([^"]*)"|(?P<value>.*))', content)
matches = re.match('(?P<key>([a-z]+(\s?))*):\s*(?:"([^"]*)"|(?P<value>.*))', content)
matches = re.search('(?P<key>([a-z]+(\s?))*):\s*(?:"([^"]*)"|(?P<value>.*))', content)

r = re.compile('(?P<key>([a-z]+(\s?))*):\s*(?:"([^"]*)"|(?P<value>.*))')
matches = [m.groupdict() for m in r.finditer(content)]

wg_key_value = dict()
m = None
key_value_indexes = [idx for idx, match in enumerate(matches) if match['key'] == 'peer']

key_value_pair_list = []
for idx, key_index in enumerate(key_value_indexes):
    if idx == len(key_value_indexes) - 1:
        key_value_pair_list.append(
            matches[key_index:]
        )
    else:
        key_value_pair_list.append(
            matches[key_index: key_value_indexes[idx + 1]]
        )


pass

# def lindexsplit(some_list, *args):
#     # Checks to see if any extra arguments were passed. If so,
#     # prepend the 0th index and append the final index of the
#     # passed list. This saves from having to check for the beginning
#     # and end of args in the for-loop. Also, increment each value in
#     # args to get the desired behavior.
#     if args:
#         args = (0,) + tuple(data+1 for data in args) + (len(some_list)+1,)
#
#     # For a little more brevity, here is the list comprehension of the following
#     # statements:
#     #    return [some_list[start:end] for start, end in zip(args, args[1:])]
#     my_list = []
#     for start, end in zip(args, args[1:]):
#         my_list.append(some_list[start:end])
#     return my_list
#
# d = lindexsplit(matches, *key_value_indexes)
#
#     # if match['key'] == 'peer':
#     #     wg_key_value[] = match['value']
#
#
#
# for m in matches:
#    g = m.match
#
#    pass