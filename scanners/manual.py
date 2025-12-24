import scanners.lib.script
from scanners.lib.config import read_json
from scanners.lib.remote import form_remote_props


def generate_manual_remote(host):
    output_json = {}
    manual_config_path = "./data/" + host + "/manual/config.json"
    games = read_json(manual_config_path)
    for game in games:
        script_name = games[game].split("/")[-1]
        asset = scanners.lib.script.get_script_path(script_name, "remote")[0]
        output_json[game] = {"script": "", "asset": asset}
        form_remote_props(output_json, game, host)
    return output_json

def generate_manual_local():
    local_configs = read_json("./config/local.json")
    output_json = {}
    for game in local_configs:
        script_path, _ = scanners.lib.script.get_script_path(game, "local")
        output_json[game] = {"script": script_path}
    return output_json