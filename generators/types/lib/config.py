import json

def read_text(file_name):
    with open(file_name,'r') as f:
        return f.read().strip()

def read_json(path):
    with open(path, 'r') as file:
        return json.load(file)

def write_json(path, data):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(data, indent=4))