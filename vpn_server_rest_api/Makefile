#ifneq (,$(wildcard ./.env))
#include .env
#export
#ENV_FILE_PARAM = --env-file .env

#endif

send-script:
	sshpass -p "Qq654321" scp ./scripts/wireguard.sh  root@194.87.140.181:/root

wg:
	sudo bash ./scripts/wireguard.sh profile add --name Lol_2 --ipv4 10.66.66.119 --ipv6 fd42:42:42


