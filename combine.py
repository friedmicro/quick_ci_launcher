import copy
import json

from config_lib.athena import AthenaConfigItem
from config_lib.manual import ManualConfig


def process_partials(dictionary, browser_json_copy):
    for key in dictionary:
        config_item = AthenaConfigItem(dictionary[key])
        if not config_item.is_partial() or "script" in config_item:
            continue
        if config_item.is_partial():
            with open(dictionary[key]["partial"], "r") as file:
                partial_json = json.load(file)
            browser_json_copy[key] = partial_json
        elif not config_item.has_script_override():
            process_partials(dictionary[key], browser_json_copy[key])


with open(ManualConfig.target_config, "r") as file:
    browser_json = json.load(file)

# Python will not let us modify the reference here, pass in a copy
browser_json_copy = copy.deepcopy(browser_json)
process_partials(browser_json, browser_json_copy)
browser_json = browser_json_copy

browser_config_to_write = json.dumps(browser_json, indent=4)

with open(ManualConfig.target_config, "w") as outfile:
    outfile.write(browser_config_to_write)
