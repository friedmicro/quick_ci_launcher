import copy
import subprocess
import time
from pathlib import Path

from config_lib.athena import AthenaConfigItem
from lib.config import read_json, write_json

daemon_lock = "./client-daemon.lock"
state_file = "./state.json"
# By default keep the remote on for 5 minutes
time_per_shutdown = 60 * 5


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
        }
        subprocess.run([selected_item.start_script], shell=True)
    else:
        state[selected_item.ip]["last_action_time"] = time.time()
        state[selected_item.ip]["operation"] = "start"
    write_state(state)


def stop_remote(selected_item: AthenaConfigItem):
    if should_execute_as_client(selected_item):
        if selected_item.has_stop_script():
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
                subprocess.run([host_info["stop_script"]], shell=True)
                write_state(state_copy)


# For if a user wants to end the remote immediately; ex: in a script
def force_stop_remote(ip):
    state = load_state()
    stop_script = state[ip]["stop_script"]
    del state[ip]
    write_state(state)
    subprocess.run([stop_script], shell=True)


def remove_tracking(ip):
    state = load_state()
    del state[ip]
    write_state(state)
