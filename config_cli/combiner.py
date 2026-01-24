import json

from config_lib.combiner import CombinerConfig
from lib.cli import parse_params


def combiner(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=False)
    _, multiple_args, _ = parse_params(params, argument_is_json=False, param_count=2)
    combiner_config = CombinerConfig(is_client)
    match operation:
        case "get_time_limit":
            print(json.dumps(combiner_config.get_time_limit(arguments)))
        case "update_time_limit":
            combiner_config.update_time_limit(multiple_args[0], multiple_args[1])
            print("Config updated successfully")
        case "fetch_time_limit":
            print(combiner_config.fetch_time_exceptions(arguments))
        case "update_time_exceptions":
            combiner_config.update_time_exceptions(multiple_args[0], multiple_args[1])
            print("Config updated successfully")
        case "fetch_time_files":
            print(combiner_config.fetch_time_files(arguments))
        case "update_time_files":
            combiner_config.update_time_files(multiple_args[0], multiple_args[1])
            print("Config updated successfully")
        case "fetch_time_schedule":
            print(json.dumps(combiner_config.fetch_time_schedule(arguments)))
        case "update_time_schedule":
            combiner_config.update_time_schedule(multiple_args[0], multiple_args[1])
            print("Config updated successfully")
        case "fetch_files":
            print(combiner_config.fetch_files())
        case "add_file":
            combiner_config.add_combiner_file(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
