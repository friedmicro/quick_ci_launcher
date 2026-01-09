import json

from config_lib.athena import AthenaConfig
from lib.config import read_json, write_json


class CombinerTimeException(dict):
    def __init__(self, time_exception) -> None:
        self.day = time_exception["day"]
        self.start_time = time_exception["start_time"]
        self.end_time = time_exception["end_time"]
        dictionary_map = {
            "day": self.day,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
        super().__init__(self, **dictionary_map)


class CombinerFile(dict):
    def __init__(self, config_object) -> None:
        self.files = config_object["files"]
        self.time_limit = config_object["time_limit"]
        self.time_exceptions = config_object["time_exceptions"]

        time_exceptions = config_object["time_exceptions_schedule"]
        time_exceptions_schedule = {}
        for schedule in time_exceptions:
            time_exceptions_schedule[schedule] = CombinerTimeException(
                time_exceptions[schedule]
            )
        self.time_exceptions_schedule = time_exceptions_schedule

        dictionary_map = {
            "files": self.files,
            "time_limit": self.time_limit,
            "time_exceptions": self.time_exceptions,
            "time_exceptions_schedule": self.time_exceptions_schedule,
        }
        super().__init__(self, **dictionary_map)

    def __getattr__(self, attr):
        return self[attr]


# Technically this class both generates the athena launcher config
# and also allows updating properties. This is not ideal as it mixes
# responsiblities, but for now it is simpler (one config object per setting file)
# to leave it this way. If we do refactor into multiple files then split this out.
class CombinerConfig:
    manual_config_path = "./config/combiner.json"

    def __init__(self, is_client=False) -> None:
        self.is_client = is_client
        config_data = read_json(self.manual_config_path, is_client)
        self.file_data = config_data
        files = {}
        for datum in config_data:
            files[datum] = CombinerFile(config_data[datum])
        self.files = files

    # Call this to create a map object containing the configuration data
    def merge_partials(self):
        output_json = {}
        for combination in self.files:
            combination_data = self.files[combination]
            json_files = combination_data.files
            for file_name in json_files:
                with open(file_name, "r") as file:
                    file_json = json.load(file)
                output_json = output_json | file_json
        self.config_json = output_json

    # Call this to create a format athena can read
    # Returns an array for filtering purposes, call
    # convert_to_config_map once done
    def process_simple_and_complex_files(self):
        temp_list = []
        athena_config = AthenaConfig()
        for key, item in self.config_json.items():
            # User has defined a valid data structure; allow populate full config
            if (
                "asset" in item
                or "emulator" in item
                or "script" in item
                or "web" in item
            ):
                json_item = {"name": key}
                for setting in item:
                    json_item[setting] = item[setting]
                temp_list.append(json_item)
            # Assume simple config, this is to allow simple plugins
            else:
                config = athena_config.generate_script(item)
                config["name"] = key
                temp_list.append(config)
        return temp_list

    # Convert array of program config to a dictionary that athena
    # can process; applies modification settings for the file
    def convert_to_config_map(self, config_array, combination_data):
        tmp_json = {}
        for item in config_array:
            item_name = item["name"]
            tmp_json[item_name] = item
            tmp_json[item_name]["time_limit"] = combination_data.time_limit
            if item_name in combination_data.time_exceptions:
                tmp_json[item_name]["time_limit"] = not combination_data.time_limit
            if item_name in combination_data.time_exceptions_schedule:
                tmp_json[item_name]["time_schedule"] = (
                    combination_data.time_exceptions_schedule[item_name]
                )
            del tmp_json[item_name]["name"]
        return tmp_json

    def write_config(self):
        if self.is_client:
            write_json(self.manual_config_path, self.file_data, client_write=True)
        else:
            write_json(self.manual_config_path, self.file_data)

    # Operations on the data structure
    def get_time_limit(self, file):
        return self.file_data[file]["time_limit"]

    def update_time_limit(self, file, state):
        self.file_data[file]["time_limit"] = state
        self.write_config()

    def fetch_time_exceptions(self, file):
        return self.file_data[file]["time_exceptions"]

    def update_time_exceptions(self, file, exceptions):
        self.file_data[file]["time_exceptions"] = exceptions
        self.write_config()

    def fetch_time_files(self, file):
        return self.file_data[file]["files"]

    def update_time_files(self, file, files):
        self.file_data[file]["files"] = files
        self.write_config()

    def fetch_time_schedule(self, file):
        return self.file_data[file]["time_schedule"]

    def update_time_schedule(self, file, schedule):
        self.file_data[file]["time_schedule"] = schedule
        self.write_config()

    # Add combiner file; by default all properties are unset
    def add_combiner_file(self, file):
        self.file_data[file] = {
            "time_limit": False,
            "time_exceptions": {},
            "time_exceptions_schedule": {},
            "files": [],
            "time_schedule": [],
        }
        self.write_config()
