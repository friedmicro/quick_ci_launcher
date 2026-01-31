import json

from config_lib.emulators import EmulatorConfig
from lib.cli import parse_params


def emulators(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=False)
    emulator_config = EmulatorConfig(is_client)
    match operation:
        case "fetch_remapping":
            print(json.dumps(emulator_config.fetch_remapping()))
        case "update_remapping":
            emulator_config.update_remapping(arguments)
            print("Config updated successfully")
        case "fetch_selected":
            print(json.dumps(emulator_config.fetch_selected()))
        case "update_selected":
            emulator_config.update_selected(arguments)
            print("Config updated successfully")
        case "fetch_emulators":
            print(json.dumps(emulator_config.fetch_emulators()))
        case "fetch_emulator":
            print(json.dumps(emulator_config.fetch_emulator(arguments)))
        case "update_emulator":
            _, arguments, _ = parse_params(
                params, argument_is_json=False, param_count=2
            )
            emulator_config.update_emulator(arguments[0], json.loads(arguments[1]))
            print("Config updated successfully")
        case "add_emulator":
            emulator_config.add_emulator(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
