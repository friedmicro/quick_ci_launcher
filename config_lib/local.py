from config_lib.athena import AthenaConfig
from lib.config import read_json, write_json
from lib.script import get_script_path


class LocalConfig:
    manual_config = "./config/local.json"

    def __init__(self):
        self.config_data = read_json(self.manual_config)

    def fetch_local(self):
        return self.config_data

    def update_local(self, new_config):
        self.config_data = new_config
        write_json(self.manual_config, self.config_data)

    def generate_config_object(self, game):
        script_path, _ = get_script_path(game, "local")
        return AthenaConfig().generate_script(script_path)
