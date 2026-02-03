import copy
import subprocess
import sys
import time
from pathlib import Path

from config_lib.athena import AthenaConfigItem
from config_lib.client import GeneratorConfig
from lib.config import read_json, write_json

config = read_json("./config/client_daemon.json")

daemon_lock = "./client-daemon.lock"
state_file = config["state_path"]
time_per_shutdown = config["time_per_shutdown"]


# Add an indicator so that clients know if the client daemon is installed
def init_client_daemon():
    Path(daemon_lock).touch()


def is_daemon_installed():
    return Path(daemon_lock).exists()


def load_state():
    return read_json(state_file)


def write_state(state):
    write_json(state_file, state)


def should_execute_as_client(selected_item: AthenaConfigItem):
    return (
        not selected_item.has_stop_script()
        or not selected_item.has_start_script()
        and is_daemon_installed()
    )


def start_remote(selected_item: AthenaConfigItem):
    if should_execute_as_client(selected_item):
        if selected_item.has_start_script():
            subprocess.run([selected_item.start_script], shell=True)
        return
    state = load_state()
    if selected_item.ip not in state:
        state[selected_item.ip] = {
            "last_action_time": time.time(),
            "operation": "start",
            "start_script": selected_item.start_script,
            "stop_script": selected_item.stop_script,
            "force_sync": selected_item.force_sync,
        }
        subprocess.run([selected_item.start_script], shell=True)
    else:
        state[selected_item.ip]["last_action_time"] = time.time()
        state[selected_item.ip]["operation"] = "start"
    write_state(state)


def stop_remote(selected_item: AthenaConfigItem):
    if should_execute_as_client(selected_item) or selected_item.skip_daemon:
        if selected_item.has_stop_script():
            if selected_item.force_sync:
                generator_config = GeneratorConfig()
                subprocess.run(generator_config.generator_path)
            subprocess.run([selected_item.stop_script], shell=True)
        return
    state = load_state()
    state[selected_item.ip]["last_action_time"] = time.time()
    state[selected_item.ip]["operation"] = "stop"
    write_state(state)


def parse_state():
    state = load_state()
    state_copy = copy.deepcopy(state)
    for host in state:
        host_info = state[host]
        current_time = time.time()
        last_action_time = host_info["last_action_time"]
        if current_time - last_action_time > time_per_shutdown:
            if host_info["operation"] == "stop":
                del state_copy[host]
                if host_info["force_sync"]:
                    generator_config = GeneratorConfig()
                    subprocess.run(generator_config.generator_path)
                subprocess.run([host_info["stop_script"]], shell=True)
                write_state(state_copy)


def validate_ip(state, ip):
    if ip not in state:
        print("IP not found in state")
        sys.exit(0)


# For if a user wants to end the remote immediately; ex: in a script
def force_stop_remote(ip):
    state = load_state()
    validate_ip(state, ip)
    stop_script = state[ip]["stop_script"]
    del state[ip]
    write_state(state)
    subprocess.run([stop_script], shell=True)


def remove_tracking(ip):
    state = load_state()
    validate_ip(state, ip)
    del state[ip]
    write_state(state)
