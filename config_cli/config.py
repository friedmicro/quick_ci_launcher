from config_cli.android import android
from config_cli.athena import athena


def config(params: list[str]):
    config_class = str(params[0])
    match config_class:
        case "android":
            android(params[1:])
        case "athena":
            athena(params[1:])
        case "client":
            pass
        case "combiner":
            pass
        case "emulators":
            pass
        case "local":
            pass
        case "manual":
            pass
        case "overrides":
            pass
        case "remote":
            pass
        case "steam":
            pass
        case "web":
            pass
        case "windows_games":
            pass
        case _:
            print("Not a valid option")
