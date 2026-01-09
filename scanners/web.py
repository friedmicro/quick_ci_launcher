from config_lib.athena import AthenaConfig
from config_lib.web import WebConfig


def generate_web_pages():
    output_json = {}
    athena_config = AthenaConfig()
    web_config = WebConfig()
    games = web_config.fetch_programs()
    for game in games:
        output_json[game] = athena_config.generate_web(
            games[game], web_config.fetch_check_ip()
        )
    return output_json
