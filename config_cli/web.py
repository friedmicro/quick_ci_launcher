import json

from config_lib.web import WebConfig
from lib.cli import parse_params


def web(params):
    operation, argument, is_client = parse_params(params, argument_is_json=False)
    web_config = WebConfig(is_client)
    match operation:
        case "fetch_programs":
            print(json.dumps(web_config.fetch_programs()))
        case "fetch_browser":
            print(json.dumps(web_config.fetch_browser()))
        case "fetch_close_existing":
            print(web_config.fetch_close_existing())
        case "fetch_kiosk":
            print(web_config.fetch_kiosk())
        case "fetch_check_ip":
            print(web_config.fetch_check_ip())
        case "update_config":
            _, json_arg, _ = parse_params(params, argument_is_json=True)
            web_config.update_config(json_arg)
            print("Config updated successfully")
        case "update_browser":
            web_config.update_browser(argument)
            print("Config updated successfully")
        case "update_close_existing":
            web_config.update_close_existing(argument)
            print("Config updated successfully")
        case "update_kiosk":
            web_config.update_kiosk(argument)
            print("Config updated successfully")
        case "update_check_ip":
            web_config.update_check_ip(argument)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
