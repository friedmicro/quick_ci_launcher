from lib.config import read_json, write_json


class OverridesConfig:
    manual_config_path = "./config/overrides.json"

    def __init__(self) -> None:
        self.config_data = read_json(self.manual_config_path)
        pass

    def fetch_overrides(self):
        return self.config_data

    def update_overrides(self, new_data):
        self.config_data = new_data
        write_json(self.manual_config_path, self.config_data)
