import json

from config_lib.android import AndroidConfig


def android(params):
    android_config = AndroidConfig()
    func = params[0]
    match func:
        case "load_apps":
            print(json.dumps(android_config.load_apps()))
        case "update_config":
            apps = params[1]
            android_config.update_config(apps)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
