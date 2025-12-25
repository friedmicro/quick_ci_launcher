import json
import os

def read_text(file_name):
    with open(file_name,'r') as f:
        return f.read().strip()

def read_json(path):
    with open("./config/client.json", 'r') as file:
        client_config = json.load(file)
        client_id = client_config["id"]
        entire_overrides = client_config["local_overrides_entire"]
    with open(path, 'r') as file:
        global_config = json.load(file)
    client_path = path.replace("./config/", "./config/clients/" + client_id + "/")
    if os.path.exists(client_path):
        with open(client_path, 'r') as file:
            client_config = json.load(file)
        if path in entire_overrides:
            return client_config
        else:
            for key in client_config:
                global_config[key] = client_config[key]
    return global_config

def write_json(path, data):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(data, indent=4))