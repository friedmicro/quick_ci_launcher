from config_lib.athena import AthenaConfig
from lib.config import read_json, write_json


class AndroidConfig:
    manual_config_path = "./config/android.json"

    def __init__(self) -> None:
        pass

    def load_config_map(self):
        output_json = {}
        games = read_json(self.manual_config_path)
        athena_config = AthenaConfig()
        for game in games:
            output_json[game] = athena_config.generate_waydroid(games[game])
        return output_json

    def load_apps(self):
        return read_json(self.manual_config_path)

    # Take apps, update config...assumes json object, no validation
    def update_config(self, apps):
        write_json(self.manual_config_path, apps)
