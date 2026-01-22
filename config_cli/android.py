import json

from config_lib.android import AndroidConfig
from lib.cli import parse_params


def android(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=True)
    android_config = AndroidConfig(is_client)
    match operation:
        case "load_apps":
            print(json.dumps(android_config.load_apps()))
        case "update_config":
            android_config.update_config(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
