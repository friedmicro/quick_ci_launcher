import os

import scanners.lib.script
import scanners.lib.template
from scanners.lib.config import read_json
from scanners.lib.remote import form_remote_props

remote_config = read_json("./config/remote.json")
steam_config = read_json("./config/steam.json")


def search_exclusions(name):
    for exclusion in steam_config["exclude"]:
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
        if name in steam_config["remapping"]:
            name = steam_config["remapping"][name]
        if search_exclusions(name):
            continue
        game = {"app_id": app_id, "name": name}
        games_found.append(game)
    return games_found


output_json = {}


def form_game_template(game, host, mode):
    os_in_use = steam_config[host]["os"]
    launch_command = steam_config[host][mode]
    if os_in_use == "linux":
        return """{shebang}
{launch_command} steam://rungameid/{app_id}""".format(
            shebang=scanners.lib.template.bash(),
            launch_command=launch_command,
            app_id=game["app_id"],
        )
    elif os_in_use == "windows":
        return """{launch_command} steam://rungameid/{app_id}""".format(
            launch_command=launch_command, app_id=game["app_id"]
        )


def parse_acf(host, mode):
    steam_native = "./data/" + host + "/acf/" + mode
    games_native = locate_games(steam_native)

    for game in games_native:
        script_template = form_game_template(game, host, mode)
        output_json[game["name"]] = {}
        output_json[game["name"]]["asset"] = scanners.lib.script.write(
            game["app_id"], script_template, "remote"
        )
        output_json[game["name"]]["script"] = ""
        form_remote_props(output_json, game["name"], host)

    return output_json
