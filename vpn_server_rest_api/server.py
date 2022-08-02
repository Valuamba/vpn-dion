import os.path
import os
from flask import Flask, send_file

from statistics.collect_statistics import get_ram, get_network_statistics, get_cpu
from statistics.models import ServerStatistic
from config import Config
from wireguard.wireguard_service import add_client_config, remove_client

app = Flask(__name__)


@app.route("/addClient/<client_name>")
def add_client(client_name: str):
    response = add_client_config(client_name)
    return response


@app.route("/removeClient/<client_name>")
def remove_client_post(client_name: str):
    response = remove_client(client_name)
    return response


@app.route("/collect-statistics")
def collect_statistic():
    ram = get_ram()
    cpu = get_cpu()
    upload, download, total, upload_speed, down_speed = get_network_statistics()
    server_statistic = ServerStatistic(network_upload=upload,
                                       network_download=download,
                                        total=total,
                                        network_upload_speed=upload_speed,
                                        network_download_speed=down_speed,
                                        ram=ram,
                                        cpu=cpu)

    return server_statistic.__dict__



if __name__ == "__main__":
    port = Config.VPN_SERVER_PORT
    app.run(debug=True, host='0.0.0.0', port=port)