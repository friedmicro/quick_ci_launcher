import json
import copy

def process_partials(dictionary, browser_json_copy):
    for key in dictionary:
        if "partial" in dictionary[key]:
            with open(dictionary[key]["partial"], "r") as file:
                partial_json = json.load(file)
            browser_json_copy[key] = partial_json
        elif not "script" in dictionary[key]:
            process_partials(dictionary[key], browser_json_copy[key])

with open("config.json", 'r') as file:
    browser_json = json.load(file)

# Python will not let us modify the reference here, pass in a copy
browser_json_copy = copy.deepcopy(browser_json)
process_partials(browser_json, browser_json_copy)
browser_json = browser_json_copy

browser_config_to_write = json.dumps(browser_json, indent=4)

with open("config.json", "w") as outfile:
    outfile.write(browser_config_to_write)