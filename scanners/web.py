from scanners.lib.config import read_json


def generate_web_pages():
    output_json = {}
    manual_config_path = "./config/web.json"
    games = read_json(manual_config_path)["games"]
    for game in games:
        output_json[game] = {"script": "", "web": games[game]}
    return output_json
