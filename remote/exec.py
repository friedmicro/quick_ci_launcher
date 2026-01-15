import multiprocessing
import subprocess

from config_lib.athena import AthenaConfigItem
from config_lib.remote import RemoteConfig
from launcher.daemon_comm import send_asset, send_start, send_stop


def daemon_start(selected_item: AthenaConfigItem):
    if selected_item.athena_installed:
        start_thread = multiprocessing.Process(
            target=send_start, args=(selected_item.ip,)
        )
        start_thread.start()
        if not selected_item.skip_assets:
            asset_thread = multiprocessing.Process(
                target=send_asset,
                args=(
                    selected_item.ip,
                    selected_item.asset,
                    selected_item.os,
                ),
            )
            asset_thread.start()


def daemon_stop(selected_item: AthenaConfigItem):
    if selected_item.athena_installed and not selected_item.skip_stop_command:
        send_stop(selected_item.ip)


def launch_client_app(selected_item: AthenaConfigItem):
    remote_config = RemoteConfig()
    if selected_item.remote_client_type == "moonlight":
        moonlight_command = (
            remote_config.fetch_defaults()["moonlight_client_path"]
            + " stream "
            + selected_item.moonlight_machine
            + " "
            + selected_item.moonlight_app
        )
        subprocess.run([moonlight_command], shell=True)
    elif selected_item.remote_client_type == "rdp":
        rdp_command = remote_config.fetch_defaults()["rdp_client_exec"]
        rdp_command = rdp_command.replace("{ip}", selected_item.ip)
        rdp_command = rdp_command.replace("{user}", selected_item.user)
        subprocess.run([rdp_command], shell=True)


def execute_client_remote(selected_item: AthenaConfigItem):
    daemon_start(selected_item)
    launch_client_app(selected_item)
    daemon_stop(selected_item)
