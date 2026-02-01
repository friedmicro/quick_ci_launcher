from config_cli.android import android
from config_cli.athena import athena
from config_cli.client import client
from config_cli.combiner import combiner
from config_cli.emulators import emulators
from config_cli.local import local
from config_cli.manual import manual
from config_cli.overrides import overrides


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
            emulators(args)
        case "local":
            local(args)
        case "manual":
            manual(args)
        case "overrides":
            overrides(args)
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
