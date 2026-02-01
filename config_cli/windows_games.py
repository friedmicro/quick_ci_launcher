from config_lib.windows_games import WindowsGamesConfig
from lib.cli import parse_params


def windows_games(params):
    operation, arguments, is_client = parse_params(params, argument_is_json=False)
    windows_games_config = WindowsGamesConfig(is_client)
    match operation:
        case "fetch_exclude":
            print(windows_games_config.fetch_exclude())
        case "update_exclude":
            windows_games_config.update_exclude(arguments.split(","))
            print("Config updated successfully")
        case "fetch_open_steam_direct":
            windows_games_config.fetch_open_steam_direct()
        case "update_open_steam_direct":
            windows_games_config.update_open_steam_direct(arguments.split(","))
            print("Config updated successfully")
        case "fetch_steam_path":
            windows_games_config.fetch_steam_path()
        case "update_steam_path":
            windows_games_config.update_steam_path(arguments)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
