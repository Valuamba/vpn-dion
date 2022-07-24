import os.path
import os
from flask import Flask, send_file

from vpn_server_rest_api.wireguard.wireguard_service import add_client_config

app = Flask(__name__)


@app.route("/addClient/<client_name>")
def hello_world(client_name: str):
    response = add_client_config(client_name)


if __name__ == "__main__":
    port = int(os.environ.get('IMAGE_SERVER_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)