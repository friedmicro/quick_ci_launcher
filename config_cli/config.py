from config_cli.android import android
from config_cli.athena import athena
from config_cli.client import client
from config_cli.combiner import combiner


def config(params: list[str]):
    config_class = str(params[0])
    args = params[1:]
    match config_class:
        case "android":
            android(args)
        case "athena":
            athena(args)
        case "client":
            client(args)
        case "combiner":
            combiner(args)
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
