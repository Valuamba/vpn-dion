import enum
import re
import sys

import pexpect


class Options(enum.IntEnum):
    AddNewUser = 1
    RevokeExistingUser = 2
    UninstallWireGuard = 3
    Exit = 4


select_option = "Select an option [1-4]: "
client_name = "Client name:"
wireguard_ipv4 = "Client's WireGuard IPv4:"
wireguard_ipv6 = "Client's WireGuard IPv6:"

child = pexpect.spawn('../scripts/wireguard-install.sh', encoding='utf-8')
child.logfile = sys.stdout
child.expect(f'.*{re.escape(select_option)}.*')
child.send("1\n")
child.expect(client_name)
child.send('Valentin6mes\n')
child.expect(wireguard_ipv4)
child.send('\n')
child.expect(wireguard_ipv6)
child.send('\n')

print(child.read())
