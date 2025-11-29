import json

with open("config/combiner.json", "r") as file:
    combined_files = json.load(file)

for combination in combined_files:
    output_json = {}
    json_files = combined_files[combination]["files"]
    for file_name in json_files:
        with open(file_name, "r") as file:
            file_json = json.load(file)
        output_json = output_json | file_json

    temp_list = []
    for key, item in output_json.items():
        if "asset" in item:
            json_item = {
                "asset": item["asset"],
                "name": key
            }
            if "ip" in item:
                json_item["ip"] = item["ip"]
            if "remote_client_path" in item:
                json_item["remote_client_path"] = item["remote_client_path"][
                    "remote_client_path"
                ]
            if "remote_client_type" in item:
                json_item["remote_client_type"] = item["remote_client_type"][
                    "remote_client_type"
                ]
            if "moonlight_app" in item:
                json_item["moonlight_app"] = item["moonlight_app"]
            if "start_script" in item:
                json_item["start_script"] = item["start_script"]
            if "stop_script" in item:
                json_item["stop_script"] = item["stop_script"]
            if "script" in item:
                json_item["script"] = item["script"]
            temp_list.append(json_item)
        else:
            temp_list.append({"name": key, "script": item})

    # Sort partials and create config objects
    temp_list = sorted(temp_list, key=lambda x: x["name"], reverse=False)
    tmp_json = {}
    for item in temp_list:
        tmp_json[item["name"]] = item
        tmp_json[item["name"]]["time_limit"] = combined_files[combination]["time_limit"]
        if item["name"] in combined_files[combination]["time_exceptions"]:
            tmp_json[item["name"]]["time_limit"] = not combined_files[combination]["time_limit"]
        del tmp_json[item["name"]]["name"]

    with open(combination, "w") as outfile:
        outfile.write(json.dumps(tmp_json, indent=4))