import datetime
import multiprocessing
import os
import platform
import subprocess
import time

from config_lib.athena import AthenaConfigItem
from config_lib.remote import RemoteConfig
from config_lib.web import WebConfig
from launcher.config_lib.emulators import EmulatorConfig
from launcher.daemon_comm import send_asset, send_start, send_stop
from launcher.lib.config import read_json, write_json
from launcher.time_keep import is_item_time_whitelisted, time_counter_loop

time_configuration = read_json("./config/time_config.json")
time_ledger = read_json("time.json")


def execute_program_with_time_logging(selected_item):
    time_saver_trigger = time_configuration["time_saver_trigger"]

    if os.path.exists(time_saver_trigger):
        week_number = int(datetime.datetime.today().strftime("%V"))
        if time_ledger["week_number"] != week_number:
            time_ledger["week_number"] = week_number
            time_ledger["ledger"] = {}
        today = datetime.datetime.today()
        day_of_week = str(today.weekday())
        if day_of_week not in time_ledger["ledger"]:
            time_ledger["ledger"][day_of_week] = {}

        start_time = int(time.time())

        current_time_total = 0
        for time_record in time_ledger["ledger"][day_of_week]:
            current_time_total += time_ledger["ledger"][day_of_week][time_record] - int(
                time_record
            )

        print(current_time_total)

        if current_time_total >= time_configuration["first_warning_time"]:
            print(time_configuration["time_limit_reached"])
            return

        time_ledger["ledger"][day_of_week][start_time] = None

        thread = multiprocessing.Process(
            target=time_counter_loop, args=(current_time_total,)
        )
        thread.start()

    launch_program(selected_item)

    if os.path.exists(time_saver_trigger):
        end_time = int(time.time())
        time_ledger["ledger"][day_of_week][start_time] = end_time

        thread.terminate()

        write_json("time.json", time_ledger)


def launch_program(selected_item: AthenaConfigItem):
    if selected_item.has_script_override():
        subprocess.run([selected_item.script])
    elif selected_item.is_emulator():
        emulator_config = EmulatorConfig().fetch_emulator(selected_item.emulator)
        asset = selected_item.asset
        emulator_exec = emulator_config.exec.replace("{rom_path}", asset)
        subprocess.run([emulator_exec], shell=True)
    elif selected_item.is_layer():
        if selected_item.is_waydroid():
            subprocess.run(
                ["waydroid app launch " + selected_item.asset + " &"], shell=True
            )
    elif selected_item.is_web():
        web_config = WebConfig()
        os_in_use = platform.system().lower()
        if web_config.fetch_close_existing():
            kill_exec = "killall " + web_config.fetch_browser()
            if "win" in os_in_use:
                browser_binary = web_config.fetch_browser().split("/")[-1]
                kill_exec = "taskkill /IM " + browser_binary
            subprocess.run([kill_exec], shell=True)
            # Give the process time to gracefully close
            time.sleep(2)
        browser_exec = web_config.fetch_browser() + " "
        if web_config.fetch_kiosk():
            browser_exec += "--kiosk "
        browser_exec += selected_item.web
        subprocess.run([browser_exec], shell=True)
    elif selected_item.is_remote():
        remote_config = RemoteConfig()
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
        if selected_item.athena_installed:
            send_stop(selected_item.ip)


def setup_and_launch(is_logging_time, selected_item):
    selected_item = AthenaConfigItem(selected_item)
    if selected_item.has_start_script():
        subprocess.run([selected_item.start_script], shell=True)
    if is_logging_time:
        if is_item_time_whitelisted(selected_item):
            launch_program(selected_item)
        else:
            execute_program_with_time_logging(selected_item)
    else:
        launch_program(selected_item)
    if selected_item.has_stop_script():
        subprocess.run([selected_item.stop_script], shell=True)
