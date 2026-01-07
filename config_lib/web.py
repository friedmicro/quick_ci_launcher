from lib.config import read_json, write_json


class WebConfig:
    manual_config = "./config/web.json"

    def __init__(self):
        self.config = read_json(self.manual_config)

    def fetch_programs(self):
        return self.config["games"]

    def update_config(self, new_config):
        self.config["games"] = new_config
        write_json(self.manual_config, self.config)

    def fetch_browser(self):
        return self.config["browser"]

    def update_browser(self, new_browser):
        self.config["browser"] = new_browser
        write_json(self.manual_config, self.config)

    def fetch_close_existing(self):
        return self.config["close_existing"]

    def update_close_existing(self, new_close_existing):
        self.config["close_existing"] = new_close_existing
        write_json(self.manual_config, self.config)

    def fetch_kiosk(self):
        return self.config["kiosk"]

    def update_kiosk(self, new_kiosk):
        self.config["kiosk"] = new_kiosk
        write_json(self.manual_config, self.config)
