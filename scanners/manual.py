import lib.script
from config_lib.athena import AthenaConfig
from config_lib.local import LocalConfig
from lib.config import read_json


def generate_manual_remote(host):
    output_json = {}
    manual_config_path = "./data/" + host + "/manual/config.json"
    games = read_json(manual_config_path)
    athena_config = AthenaConfig()
    for game in games:
        script_name = games[game].split("/")[-1]
        asset, _ = lib.script.get_script_path(script_name, "remote")
        output_json[game] = athena_config.generate_remote(asset, host)
    return output_json


def generate_manual_local():
    local = LocalConfig()
    local_configs = local.fetch_local()
    output_json = {}
    for game in local_configs:
        output_json[game] = local.generate_config_object(game)
    return output_json
