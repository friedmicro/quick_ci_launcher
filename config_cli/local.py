import json

from config_lib.local import LocalConfig
from lib.cli import parse_params


def local(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=False)
    local_config = LocalConfig(is_client)
    match operation:
        case "update_local":
            local_config.update_local(arguments)
            print("Config updated successfully")
        case "fetch_local":
            data = local_config.fetch_local()
            print(json.dumps(data))
        case _:
            print("Not a valid option")
