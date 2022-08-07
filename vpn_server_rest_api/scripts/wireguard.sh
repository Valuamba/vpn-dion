#!/bin/bash

#set -x
#
#var=5
#while [ $var -gt 0 ]; do
#  var=$[ $var-1 ]
#  echo $var
#  sleep 2
#done

#CLIENT_NAME
#echo ""
#	echo "Tell me a name for the client."
#	echo "The name must consist of alphanumeric character. It may also include an underscore or a dash and can't exceed 15 chars."
#		read -rp "Client name: " -e CLIENT_NAME
#
##EXIT 0
#echo ""
#echo "A client with the specified name was already created, please choose another name."
#echo ""
#
#read -rp "Client's WireGuard IPv4: ${BASE_IP}." -e -i "${DOT_IP}" DOT_IP
#ead -rp "Client's WireGuard IPv6: ${BASE_IP}::" -e -i "${DOT_IP}" DOT_IP
#
#	echo "[Interface]
#PrivateKey = ${CLIENT_PRIV_KEY}
#Address = ${CLIENT_WG_IPV4}/32,${CLIENT_WG_IPV6}/128
#DNS = ${CLIENT_DNS_1},${CLIENT_DNS_2}
#
#[Peer]
#PublicKey = ${SERVER_PUB_KEY}
#PresharedKey = ${CLIENT_PRE_SHARED_KEY}
#Endpoint = ${ENDPOINT}
#AllowedIPs = 0.0.0.0/0,::/0" >>"${HOME_DIR}/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"
#
#	# Add the client as a peer to the server
#	echo -e "\n### Client ${CLIENT_NAME}
#[Peer]
#PublicKey = ${CLIENT_PUB_KEY}
#PresharedKey = ${CLIENT_PRE_SHARED_KEY}
#AllowedIPs = ${CLIENT_WG_IPV4}/32,${CLIENT_WG_IPV6}/128" >>"/etc/wireguard/${SERVER_WG_NIC}.conf"
#
#echo -e "\nHere is your client config file as a QR Code:"
#
#	qrencode -t ansiutf8 -l L <"${HOME_DIR}/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"
#
#	echo "It is also available in ${HOME_DIR}/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"
#
#	cat "${HOME_DIR}/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"

RED='\033[0;31m'
ORANGE='\033[0;33m'
NC='\033[0m'

function isRoot() {
  if [ "${EUID}" -ne 0 ]; then
    echo "You need to run this script as root"
    exit 1
  fi
}

function checkVirt() {
  if [ "$(systemd-detect-virt)" == "openvz" ]; then
    echo "OpenVZ is not supported"
    exit 1
  fi

  if [ "$(systemd-detect-virt)" == "lxc" ]; then
    echo "LXC is not supported (yet)."
    echo "WireGuard can technically run in an LXC container,"
    echo "but the kernel module has to be installed on the host,"
    echo "the container has to be run with some specific parameters"
    echo "and only the tools need to be installed in the container."
    exit 1
  fi
}

function checkOS() {
  # Check OS version
  if [[ -e /etc/debian_version ]]; then
    source /etc/os-release
    OS="${ID}" # debian or ubuntu
    if [[ ${ID} == "debian" || ${ID} == "raspbian" ]]; then
      if [[ ${VERSION_ID} -lt 10 ]]; then
        echo "Your version of Debian (${VERSION_ID}) is not supported. Please use Debian 10 Buster or later"
        exit 1
      fi
      OS=debian # overwrite if raspbian
    fi
  elif [[ -e /etc/fedora-release ]]; then
    source /etc/os-release
    OS="${ID}"
  elif [[ -e /etc/centos-release ]]; then
    source /etc/os-release
    OS=centos
  elif [[ -e /etc/oracle-release ]]; then
    source /etc/os-release
    OS=oracle
  elif [[ -e /etc/arch-release ]]; then
    OS=arch
  else
    echo "Looks like you aren't running this installer on a Debian, Ubuntu, Fedora, CentOS, Oracle or Arch Linux system"
    exit 1
  fi
}

function initialCheck() {
  isRoot
  checkVirt
  checkOS
}

function newClient() {
  ENDPOINT="${SERVER_PUB_IP}:${SERVER_PORT}"
  [ -z "$WIREGUARD_IPv4" ] && WIREGUARD_IPv4=$(echo "$SERVER_WG_IPV4" | awk -F '.' '{ print $1"."$2"."$3 }')
  [ -z "$WIREGUARD_IPv6" ] && WIREGUARD_IPv6=$(echo "$SERVER_WG_IPV6" | awk -F '::' '{ print $1 }')

  until [[ ${CLIENT_NAME} =~ ^[a-zA-Z0-9_-]+$ && ${CLIENT_EXISTS} == '0' && ${#CLIENT_NAME} -lt 16 ]]; do
    CLIENT_EXISTS=$(grep -c -E "^### Client ${CLIENT_NAME}\$" "/etc/wireguard/${SERVER_WG_NIC}.conf")

    if [[ ${CLIENT_EXISTS} == '1' ]]; then
      exit 0
    fi
  done

  for DOT_IP in {2..254}; do
    DOT_EXISTS=$(grep -c "${SERVER_WG_IPV4::-1}${DOT_IP}" "/etc/wireguard/${SERVER_WG_NIC}.conf")
    if [[ ${DOT_EXISTS} == '0' ]]; then
      break
    fi
  done

  if [[ ${DOT_EXISTS} == '1' ]]; then
    echo "The subnet configured supports only 253 clients."
    exit 1
  fi

  #	BASE_IP=$(echo "$SERVER_WG_IPV4" | awk -F '.' '{ print $1"."$2"."$3 }')
  until [[ ${IPV4_EXISTS} == '0' ]]; do
    CLIENT_WG_IPV4="${WIREGUARD_IPv4}.${DOT_IP}"
    IPV4_EXISTS=$(grep -c "$CLIENT_WG_IPV4/24" "/etc/wireguard/${SERVER_WG_NIC}.conf")

    if [[ ${IPV4_EXISTS} == '1' ]]; then
      echo "A client with the specified IPv4 was already created, please choose another IPv4."
      exit 0
    fi
  done

  #	BASE_IP=$(echo "$SERVER_WG_IPV6" | awk -F '::' '{ print $1 }')
  until [[ ${IPV6_EXISTS} == '0' ]]; do
    CLIENT_WG_IPV6="${WIREGUARD_IPv6}::${DOT_IP}"
    IPV6_EXISTS=$(grep -c "${CLIENT_WG_IPV6}/64" "/etc/wireguard/${SERVER_WG_NIC}.conf")

    if [[ ${IPV6_EXISTS} == '1' ]]; then
      echo "A client with the specified IPv6 was already created, please choose another IPv6."
      exit 0
    fi
  done

  # Generate key pair for the client
  CLIENT_PRIV_KEY=$(wg genkey)
  CLIENT_PUB_KEY=$(echo "${CLIENT_PRIV_KEY}" | wg pubkey)
  CLIENT_PRE_SHARED_KEY=$(wg genpsk)

  # Create client file and add the server as a peer
  # Create client file and add the server as a peer
  echo "[Interface]
PrivateKey = ${CLIENT_PRIV_KEY}
Address = ${CLIENT_WG_IPV4}/32,${CLIENT_WG_IPV6}/128
DNS = ${CLIENT_DNS_1},${CLIENT_DNS_2}

[Peer]
PublicKey = ${SERVER_PUB_KEY}
PresharedKey = ${CLIENT_PRE_SHARED_KEY}
Endpoint = ${ENDPOINT}
AllowedIPs = 0.0.0.0/0,::/0" >>"${HOME_DIR}/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"

  # Add the client as a peer to the server
  echo -e "\n### Client ${CLIENT_NAME}
[Peer]
PublicKey = ${CLIENT_PUB_KEY}
PresharedKey = ${CLIENT_PRE_SHARED_KEY}
AllowedIPs = ${CLIENT_WG_IPV4}/32,${CLIENT_WG_IPV6}/128" >>"/etc/wireguard/${SERVER_WG_NIC}.conf"

  wg syncconf "${SERVER_WG_NIC}" <(wg-quick strip "${SERVER_WG_NIC}")

  CONFIG_PATH="${HOME_DIR}/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"

  cp CONFIG_PATH "/var/www/html/${SERVER_WG_NIC}-client-${CLIENT_NAME}.conf"

  echo "WireGuard client config: {$CONFIG_PATH}"
}

function getCommand() {
  while [ $# -gt 0 ]; do
    case "$1" in
    add)
      COMMAND_TYPE="add_profile"
      shift 1
      ;;
    --name)
      CLIENT_NAME="$2"
      shift 2
      ;;
    --ipv4)
      WIREGUARD_IPv4="$2"
      shift 2
      ;;
    --ipv6)
      WIREGUARD_IPv6="$2"
      shift 2
      break
      ;;
    *)
      echo $"Usage: $0 $1 $2 $3 $4 $5 $6"
      exit 1
      ;;
    esac
    case "$1" in
      remove)
        COMMAND_TYPE="remove"
        shift 1
        ;;
      --name)
        CLIENT_NAME="$2"
        shift 2
        break
      ;;
      *)
        echo $"Wrong parameter"
        exit 1
      ;;
    esac
    case "$1" in
      available)
        shift 1
        ;;
      remove)
        COMMAND_TYPE="remove"
        shift 1
        ;;
      --name)
        CLIENT_NAME="$2"
        shift 2
        break
      ;;
    --home)
        HOME_DIR="$2"
        shift 2
        break
      ;;
      *)
        echo $"Wrong parameter"
        exit 1
      ;;
    esac
  done
}

function manageMenu() {
  case "${COMMAND_TYPE}" in
  'add_profile')
    newClient
    ;;
    #	2)
    #		revokeClient
    #		;;
  esac
}
echo "${COMMAND_TYPE} ${CLIENT_NAME} ${WIREGUARD_IPv4} ${WIREGUARD_IPv6}"

#  if [ $# -lt 5 ]
#  then
#    echo "No arguments supplied"
#    exit 1
#  fi

initialCheck

# Check if WireGuard is already installed and load params
if [[ -e /etc/wireguard/params ]]; then
  echo "Manage menu"
  source /etc/wireguard/params
  getCommand "$@"
  manageMenu

else
  echo "Installing wireguard"
  installWireGuard
fi
