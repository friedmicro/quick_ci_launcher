import json

from config_lib.steam import SteamConfig
from lib.cli import parse_params


def steam(params):
    operation, argument, is_client = parse_params(params, argument_is_json=False)
    steam_config = SteamConfig(is_client)
    match operation:
        case "fetch_remapping":
            print(json.dumps(steam_config.fetch_remapping()))
        case "update_remapping":
            _, json_arg, _ = parse_params(params, argument_is_json=True)
            steam_config.update_remapping(json_arg)
            print("Config updated successfully")
        case "fetch_exclude":
            print(json.dumps(steam_config.fetch_exclude()))
        case "update_exclude":
            steam_config.update_exclude(argument.split(","))
            print("Config updated successfully")
        case "fetch_host":
            print(json.dumps(steam_config.fetch_host(argument)))
        case "update_host":
            _, multiple_arguments, _ = parse_params(
                params, argument_is_json=False, param_count=2
            )
            steam_config.update_host(
                multiple_arguments[0], json.loads(multiple_arguments[1])
            )
            print("Config updated successfully")
        case _:
            print("Not a valid option")
