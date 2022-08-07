import subprocess

home = "/home/valuamba/TelegramBots/vpn-dion/vpn_server_rest_api/tests"
p = subprocess.Popen("bash ../scripts/some.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()

print(out)
print(err)
