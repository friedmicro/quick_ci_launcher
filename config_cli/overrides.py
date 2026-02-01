import json

from config_lib.overrides import OverridesConfig
from lib.cli import parse_params


def overrides(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=True)

    overrides = OverridesConfig(is_client)

    match operation:
        case "fetch_overrides":
            print(json.dumps(overrides.fetch_overrides()))
        case "update_overrides":
            overrides.update_overrides(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
