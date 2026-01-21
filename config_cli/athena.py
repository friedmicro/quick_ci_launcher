import json

from config_lib.athena import AthenaConfig


def athena(params):
    athena_config = AthenaConfig()
    func = params[0]
    match func:
        case "fetch_config":
            print(json.dumps(athena_config.fetch_config()))
        case _:
            print("Not a valid option")
