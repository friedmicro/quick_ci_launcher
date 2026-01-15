import os
import platform
import subprocess

from config_lib.client import GeneratorConfig
from config_lib.steam import SteamConfig
from daemon.lib.comm import auth
from lib.os import copy_all_contents


class InstallConfig:
    def __init__(self) -> None:
        pass


# Create the initial configs for athena if they do not exist
# we assume you are calling this at least once. This can be an empty object.
# If you don't want to configure anything (or if the user didn't provide it).
# Force will revert to factory settings!
def create_initial_configs(
    install_config: InstallConfig, force: bool = False, skip_generator: bool = False
):
    os_in_use = platform.system().lower()

    if not force and os.path.exists("./config/client.json"):
        return

    print("Assuming this is the first run of athena; creating default configs")

    copy_all_contents("./config/defaults", "./config", False, True)

    steam_config = SteamConfig()
    local_steam = steam_config.fetch_host(os_in_use)
    steam_config.update_host("local", local_steam)

    if not skip_generator:
        generator_config = GeneratorConfig()
        subprocess.run([generator_config.scanner_path], check=True)

    auth()

    # We assume the developer will need to populate each config file as desired; utility code to do this
    # will live in config_lib
    # Of note:
    # Android: Android games, requires the Android APK name and WayDroid installed (Linux only feature)
    # Client: Machine ID and advanced config logic
    # Combiner: To define partial configs which merge at build, typically used for overrides and automation
    # Emulators: Various emulation options, a user will likely need to configure these as they can be everywhere
    # Manual: This is the baseline for the menu dropdowns, overwriting this lets the user define whatever menu structure they wish
    # Overrides: Currently, this is used to overwrite autodetection of games or to allow users to add games directly to the config.
    # It can also be used to inject into partials in general
    # Remote: Remote machines, typically these are Moonlight machines, this will require the user to install the daemon on the remote
    # Steam: Steam defaults, Linux users may need to change launch commands and other platforms will likely need to change this if they
    # have moved the install location.
    # Time_Config: This is the time management system; it records how long a user has been for example playing games and locks them out.
    # Users who want this feature will need to add a file to serve as a trigger and\or possibly update the config file.
    # Web: This includes web games, specifically forming the commands to run them automatically.
    # Windows_Games: Exclude games\programs when detected, change steam install path, allow opening Steam directly instead of the app when launched
