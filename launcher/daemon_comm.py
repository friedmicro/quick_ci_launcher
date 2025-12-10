import json
import socket

from cryptography.fernet import Fernet

from launcher.lib.config import read_text


def send_daemon_message(host, message_request, timeout=None):
    PORT = 65432

    with open("initial_config.bin", "rb") as file_object:
        encrypt_pass = file_object.read()

    crypto_key = Fernet(encrypt_pass)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, PORT))
        s.settimeout(timeout)
        message_body = json.dumps(message_request).encode()
        encrypted_message = crypto_key.encrypt(message_body)
        s.sendall(encrypted_message)
        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
        s.close()


def send_stop(host):
    send_daemon_message(host, {"operation": "stop", "params": ""}, 10 * 60)


def send_start(host):
    send_daemon_message(host, {"operation": "start", "params": ""})


def send_asset(host, asset_path, remote_os):
    asset_contents = read_text(asset_path)
    game_name = "game"
    if remote_os == "linux":
        game_name += ".sh"
    elif remote_os == "windows":
        game_name += ".bat"
    message_request = {
        "operation": "asset",
        "params": {
            "path": "$home$/" + game_name,
            "contents": asset_contents,
            "is_executable": True,
        },
    }
    send_daemon_message(host, message_request)
