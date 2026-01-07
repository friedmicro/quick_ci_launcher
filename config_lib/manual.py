# This is the core config file
import os
import shutil

from lib.config import fetch_client_config_path, read_json, write_json


class ManualConfig:
    manual_config = "./config/manual.json"
    target_config = "config.json"

    def __init__(self) -> None:
        self.raw_data = read_json(self.manual_config)

    def copy_config(self, client_id):
        shutil.copyfile(self.manual_config, self.target_config)
        client_athena_config = fetch_client_config_path(self.manual_config, client_id)
        if os.path.exists(client_athena_config):
            shutil.copyfile(client_athena_config, self.target_config)
        else:
            shutil.copyfile(self.manual_config, self.target_config)

    def fetch_data(self):
        return self.raw_data

    def update_at_index(self, path: str, value) -> None:
        parts = path.split(".")
        # This should mutate the reference
        data_to_target = self.raw_data
        for index, part in enumerate(parts):
            if index == len(parts) - 1:
                data_to_target[part] = value
            else:
                data_to_target = data_to_target[part]
        self.write_to_file()

    def write_to_file(self) -> None:
        write_json(self.manual_config, self.raw_data)
