import json

from config_lib.client import ClientConfig
from lib.cli import parse_params


def client(params):
    client_config = ClientConfig()
    operation, arguments, _ = parse_params(params, argument_is_json=False)
    match operation:
        case "fetch_id":
            print(client_config.fetch_id())
        case "update_id":
            client_config.update_id(arguments)
            print("Config updated successfully")
        case "fetch_generator":
            print(json.dumps(client_config.fetch_generator()))
        case "update_generator":
            _, arguments, _ = parse_params(params, argument_is_json=True)
            client_config.update_generator(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
