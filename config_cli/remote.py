import json

from config_lib.remote import RemoteConfig
from lib.cli import parse_params


def remote(params) -> None:
    operation, arguments, is_client = parse_params(params, argument_is_json=False)
    _, multiple_params, _ = parse_params(params, argument_is_json=False)
    remote_config = RemoteConfig(is_client)
    match operation:
        case "fetch_hosts":
            print(json.dumps(remote_config.fetch_hosts()))
        case "add_host":
            remote_config.add_host(multiple_params[0], json.loads(multiple_params[1]))
            print("Config updated successfully")
        case "update_host":
            remote_config.update_host(
                multiple_params[0], json.loads(multiple_params[1])
            )
            print("Config updated successfully")
        case "fetch_scan_options":
            print(json.dumps(remote_config.fetch_scan_options()))
        case "update_scan_options":
            _, json_arg, _ = parse_params(params, argument_is_json=True)
            remote_config.update_scan_options(json_arg)
            print("Config updated successfully")
        case "fetch_remotes_to_load":
            print(json.dumps(remote_config.fetch_remotes_to_load()))
        case "update_remotes_to_load":
            remote_config.update_remotes_to_load(arguments.split(","))
            print("Config updated successfully")
        case "fetch_defaults":
            print(json.dumps(remote_config.fetch_defaults()))
        case "update_defaults":
            _, json_arg, _ = parse_params(params, argument_is_json=True)
            remote_config.update_defaults(json.loads(json_arg))
            print("Config updated successfully")
        case "fetch_prefer_local":
            print(json.dumps(remote_config.fetch_prefer_local()))
        case "update_prefer_local":
            remote_config.update_prefer_local(arguments)
            print("Config updated successfully")
        case "fetch_prefer_exceptions":
            print(json.dumps(remote_config.fetch_prefer_exceptions()))
        case "update_prefer_exceptions":
            remote_config.update_prefer_exceptions(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
