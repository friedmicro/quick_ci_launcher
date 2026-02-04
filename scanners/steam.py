import os

import lib.script
import lib.template
from config_lib.athena import AthenaConfig
from config_lib.steam import SteamConfig
from config_lib.windows_games import WindowsGamesConfig

steam_config = SteamConfig()


def search_exclusions(name):
    for exclusion in steam_config.fetch_exclude():
        if exclusion in name:
            return True
    return False


def locate_games(steam_location):
    games_found = []
    for filename in os.listdir(steam_location):
        file_path = os.path.join(steam_location, filename)
        app_id = None
        name = None
        with open(file_path, "r") as file:
            for line in file:
                if '"appid"' in line:
                    app_id = line.strip().split('"')[3]
                if '"name"' in line:
                    name = line.strip().split('"')[3]
                # Break loop if we have found everything
                if app_id != None and name != None:
                    break
        # Rename a few games that have odd names
        if name in steam_config.fetch_remapping():
            name = steam_config.fetch_remapping()[name]
        if search_exclusions(name):
            continue
        game = {"app_id": app_id, "name": name}
        games_found.append(game)
    return games_found


output_json = {}
windows_games = WindowsGamesConfig()


def form_game_template(game, host, mode):
    os_in_use = steam_config.fetch_host(host).os
    launch_command = steam_config.fetch_host(host)[mode]
    if os_in_use == "linux":
        return """{shebang}
{launch_command} steam://rungameid/{app_id}""".format(
            shebang=lib.template.bash(),
            launch_command=launch_command,
            app_id=game["app_id"],
        )
    elif os_in_use == "windows":
        if game["name"] in windows_games.fetch_open_steam_direct():
            return f'"{windows_games.fetch_steam_path()}"'
        return """\"{launch_command}\" steam://rungameid/{app_id}""".format(
            launch_command=launch_command, app_id=game["app_id"]
        )
    elif os_in_use == "darwin":
        return """{shebang}
{launch_command} steam://rungameid/{app_id}""".format(
            shebang=lib.template.zsh(),
            launch_command=launch_command,
            app_id=game["app_id"],
        )


def parse_acf(host, mode):
    steam_native = "./data/" + host + "/acf/" + mode
    games_native = locate_games(steam_native)

    athena_config = AthenaConfig()
    for game in games_native:
        script_template = form_game_template(game, host, mode)
        output_json[game["name"]] = {}
        if host == "local":
            script_path = lib.script.write(game["app_id"], script_template, "local")
            output_json[game["name"]] = athena_config.generate_script(script_path)
        else:
            asset_path = lib.script.write(game["app_id"], script_template, "remote")
            output_json[game["name"]] = athena_config.generate_remote(asset_path, host)

    return output_json
