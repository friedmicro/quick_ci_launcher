import sys

from config_lib.install import InstallConfig, create_initial_configs
from launcher.exec import setup_and_launch
from launcher.time_keep import validate_whitelisted_days
from lib.config import read_json
from remote.manage import force_stop_remote, remove_tracking


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
    launch_option = sys.argv[1]
    if launch_option == "start":
        program_to_call = sys.argv[2]
        program_args = find_program_args(all_programs, program_to_call)

        is_logging_time = False
        if program_args is None:
            sys.exit(42)
        if "time_limit" in program_args:
            if program_args["time_limit"]:
                validate_whitelisted_days()
                is_logging_time = True
        setup_and_launch(is_logging_time, program_args)
    elif launch_option == "remote":
        remote_command = sys.argv[2]
        host_to_control = sys.argv[3]
        if remote_command == "stop":
            force_stop_remote(host_to_control)
        elif remote_command == "remove_tracking":
            remove_tracking(host_to_control)
        else:
            sys.exit(42)
    else:
        sys.exit(42)


create_initial_configs(InstallConfig())
process_user_input()
