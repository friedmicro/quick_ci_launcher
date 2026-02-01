from config_cli.android import android
from config_cli.athena import athena
from config_cli.client import client
from config_cli.combiner import combiner
from config_cli.emulators import emulators
from config_cli.local import local
from config_cli.manual import manual
from config_cli.overrides import overrides
from config_cli.remote import remote
from config_cli.steam import steam
from config_cli.web import web
from config_cli.windows_games import windows_games


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
            remote(args)
        case "steam":
            steam(args)
        case "web":
            web(args)
        case "windows_games":
            windows_games(args)
        case _:
            print("Not a valid option")
