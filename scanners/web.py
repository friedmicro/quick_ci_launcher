from scanners.lib.config import read_json


def generate_web_pages():
    output_json = {}
    manual_config_path = "./config/web.json"
    games = read_json(manual_config_path)["games"]
    for game in games:
        # Let's just ping google here
        check_domain = "google.com"
        output_json[game] = {"script": "", "web": games[game], "ip": check_domain, "live_check": check_domain}
    return output_json
