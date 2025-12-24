import json
import platform
import subprocess


def form_remote_props(output_json, name, host):
    with open("./config/remote.json", "r") as file:
        remote_config = json.load(file)

    output_json[name]["ip"] = remote_config[host]["ip"]
    output_json[name]["live_check"] = remote_config[host]["live_check"]
    output_json[name]["start_script"] = remote_config[host]["start_script"]
    output_json[name]["stop_script"] = remote_config[host]["stop_script"]
    output_json[name]["script"] = ""
    output_json[name]["moonlight_app"] = remote_config[host]["moonlight_app"]
    output_json[name]["moonlight_machine"] = remote_config[host]["moonlight_machine"]
    output_json[name]["remote_client_type"] = remote_config[host]["remote_client_type"]
    output_json[name]["os"] = remote_config[host]["os"]
    return output_json


def ping_ip(host):
    param = "-n" if "win" in platform.system().lower() else "-c"
    command = ["ping", param, "1", host]
    try:
        result = subprocess.run(command, stderr=subprocess.STDOUT, timeout=1)
        return result.returncode == 0
    except:
        return False
