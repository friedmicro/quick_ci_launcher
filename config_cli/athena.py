import json

from config_lib.athena import AthenaConfig
from lib.cli import parse_params


def athena(params):
    operation, _, _ = parse_params(params, argument_is_json=True)
    athena_config = AthenaConfig()
    match operation:
        case "fetch_config":
            print(json.dumps(athena_config.fetch_config()))
        case _:
            print("Not a valid option")
