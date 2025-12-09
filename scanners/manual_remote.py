import scanners.lib.script
from scanners.lib.config import read_json
from scanners.lib.remote import form_remote_props


def generate_manual(host):
    output_json = {}
    manual_config_path = "./data/" + host + "/manual/config.json"
    games = read_json(manual_config_path)
    for game in games:
        script_name = games[game].split("/")[-1]
        asset = scanners.lib.script.get_script_path(script_name, "remote")[0]
        output_json[game] = {"script": "", "asset": asset}
        form_remote_props(output_json, game, host)
    return output_json
