import json

from config_lib.manual import ManualConfig
from lib.cli import parse_params


def manual(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=False)
    manual_config = ManualConfig(is_client)

    match operation:
        case "fetch_data":
            json.dumps(manual_config.fetch_data())
        case "update_at_index":
            _, arguments, _ = parse_params(
                params, argument_is_json=False, param_count=2
            )
            manual_config.update_at_index(arguments[0], json.loads(arguments[1]))
            print("Config updated successfully")
        case _:
            print("Not a valid option")
