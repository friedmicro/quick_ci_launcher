import json

from config_lib.client import ClientConfig


def client(params):
    client_config = ClientConfig()
    func = params[0]
    match func:
        case "fetch_id":
            print(client_config.fetch_id())
        case "update_id":
            new_id = params[1]
            client_config.update_id(new_id)
            print("Config updated successfully")
        case "fetch_generator":
            print(json.dumps(client_config.fetch_generator()))
        case "update_generator":
            new_generator = json.loads(params[1])
            client_config.update_generator(new_generator)
            print("Config updated successfully")
        case _:
            print("Not a valid option")
