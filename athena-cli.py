import sys

from config_lib.install import InstallConfig, create_initial_configs
from launcher.exec import setup_and_launch
from launcher.lib.config import read_json
from launcher.time_keep import validate_whitelisted_days


def flatten_config(config):
    all_programs = []
    for entry in config:
        if "script" not in config[entry]:
            return flatten_config(config[entry])
        else:
            config[entry]["name"] = entry
            all_programs.append(config[entry])
    return all_programs


def process_config_data():
    config = read_json("./config.json")
    return flatten_config(config)


def find_program_args(all_programs, program_to_call):
    for program in all_programs:
        if program["name"] == program_to_call:
            return program
    return None


def process_user_input():
    all_programs = process_config_data()
    program_to_call = sys.argv[1]
    program_args = find_program_args(all_programs, program_to_call)

    is_logging_time = False
    if program_args is None:
        sys.exit(42)
    if "time_limit" in program_args:
        if program_args["time_limit"]:
            validate_whitelisted_days()
            is_logging_time = True
    setup_and_launch(is_logging_time, program_args)


create_initial_configs(InstallConfig())
process_user_input()
