import enum
import os.path
import re
import sys
import configparser
import pexpect

from vpn_server_rest_api.wireguard.models import Options, ClientConfigDto

HOME_DIRECTORY = '/home/valuamba'


def add_client_config(client_name: str):
    select_option = "Select an option [1-4]: "
    client_name_text = "Client name:"
    wireguard_ipv4 = "Client's WireGuard IPv4:"
    wireguard_ipv6 = "Client's WireGuard IPv6:"

    child = pexpect.spawn('../scripts/wireguard-install.sh', encoding='utf-8')
    child.logfile = sys.stdout
    child.expect(f'.*{re.escape(select_option)}.*')
    child.send(f"{Options.AddNewUser}\n")
    child.expect(client_name_text)
    child.send(f'{client_name}\n')
    child.expect(wireguard_ipv4)
    child.send('\n')
    child.expect(wireguard_ipv6)
    child.send('\n')

    return child.read()


def build_path_to_wireguard_config(client_name):
    return os.path.join(HOME_DIRECTORY, f'wg0-client-{client_name}.conf')


def parse_wireguard_config(client_name: str) -> ClientConfigDto:
    config = configparser.ConfigParser()
    config.read(build_path_to_wireguard_config(client_name))

    return ClientConfigDto(
        private_key=config['Interface']['PrivateKey'],
        address=config['Interface']['Address'],
        dns=config['Interface']['DNS'],
        public_key=config['Peer']['PublicKey'],
        preshared_key=config['Peer']['PresharedKey'],
        endpoint=config['Peer']['Endpoint'],
        allowed_ips=config['Peer']['AllowedIPs']
    )