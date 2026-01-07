import os

import LnkParse3

from config_lib.athena import AthenaConfig
from config_lib.windows_games import WindowsGamesConfig

windows_games = WindowsGamesConfig()
windows_exclusions = windows_games.fetch_exclude()
open_steam_direct = windows_games.fetch_open_steam_direct()


# Because Steam doesn't use lnk files.
def steam_template(program_name, url_destination):
    steam_path = windows_games.fetch_steam_path()
    if program_name in open_steam_direct:
        return f'"{windows_games.fetch_steam_path()}"'
    return f"""\"{steam_path}\" {url_destination}
""".format(steam_path=steam_path, url_destination=url_destination)


def lnk_template(program_name, target, arguments):
    return """cd \"{program_name}\"
\"{target}\" {arguments}
""".format(program_name=program_name, target=target, arguments=arguments)


def write_asset(bat_name, asset_contents):
    file_path = "./scripts/assets/" + bat_name
    f = open(file_path, "w")
    f.write(asset_contents)
    f.close()
    return file_path


def parse_lnk(host):
    games_json = {}
    directory_path = "./data/" + host + "/lnk/native"
    entries = os.listdir(directory_path)
    athena_config = AthenaConfig()
    for file_name in entries:
        program_name = file_name.split(".")[0]
        asset_name = program_name + ".bat"
        if program_name in windows_exclusions:
            continue
        if not (".url" in file_name or ".lnk" in file_name):
            continue
        asset_path = ""
        if ".url" in file_name:
            with open(f"{directory_path}/{file_name}", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "URL" in line:
                        if "steam" not in line:
                            continue
                        url_destination = line.split("URL=")[1].strip()
                        contents = steam_template(program_name, url_destination)
                        asset_path = write_asset(asset_name, contents)
        elif ".lnk" in file_name:
            lnk_file = open(f"{directory_path}/{file_name}", "rb")
            lnk = LnkParse3.lnk_file(lnk_file)
            working_directory = lnk.get_json()["data"]["working_directory"]
            target = lnk.get_json()["link_info"]["local_base_path"]
            arguments = ""
            if "command_line_arguments" in lnk.get_json()["data"]:
                arguments = lnk.get_json()["data"]["command_line_arguments"]
            contents = lnk_template(working_directory, target, arguments)
            asset_path = write_asset(asset_name, contents)
        games_json[program_name] = athena_config.generate_remote(asset_path, host)

    return games_json
