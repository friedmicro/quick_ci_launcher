import json

with open("config/combiner.json", "r") as file:
    combined_files = json.load(file)

for key in combined_files:
    output_json = {}
    json_files = combined_files[key]["files"]
    for file_name in json_files:
        with open(file_name, "r") as file:
            file_json = json.load(file)
        output_json = output_json | file_json

    temp_list = []
    for k, v in output_json.items():
        temp_list.append({"name": k, "script": v})

    # Sort partials and create config objects
    temp_list = sorted(temp_list, key=lambda x: x["name"], reverse=False)
    tmp_json = {}
    for item in temp_list:
        tmp_json[item["name"]] = {
            "script": item["script"],
            "time_limit": combined_files[key]["time_limit"]
        }
        if item["name"] in combined_files[key]["time_exceptions"]:
            tmp_json[item["name"]]["time_limit"] = not combined_files[key]["time_limit"]

    with open(key, "w") as outfile:
        outfile.write(json.dumps(tmp_json, indent=4))