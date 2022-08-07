import os

# from config import Config
import subprocess

from config import Config
from response_model import ResponseModel
from flask import current_app as app


def add_client_wireguard(client_name, ipv4=None, ipv6=None) -> ResponseModel:
    if os.path.exists(os.path.join(Config.HOME_DIRECTORY, Config.TEMPLATE_WIREGUARD % client_name)):
        raise Exception(f'Wireguard config for client name {client_name} already exists.')

    args = []
    args.append("bash")
    args.append(Config.WIREGUARD_SCRIPT_PATH)
    args.append("add")
    args.append(f"--name {client_name}")
    if ipv4:
        args.append(f"--ipv4 {ipv4}")
    elif ipv6:
        args.append(f"--ipv6 {ipv6}")

    # path = "../scripts/some1.sh"
    # args = f"bash {path}"
    try:
        p = subprocess.Popen(" ".join(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()

        if p.returncode == 1:
            return ResponseModel(is_successful=False, message=f"Command line exception: {out}")
        elif p.returncode > 1:
            return ResponseModel(is_successful=False, message=f"Command line exception: {err}")

        return ResponseModel(is_successful=True, message=f"Client was added: {err}")
    except Exception as e:
        app.logger.info(str(e))
        return ResponseModel(is_successful=True, message=f"Exception: {str(e)}")

