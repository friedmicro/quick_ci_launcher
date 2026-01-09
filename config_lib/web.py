from lib.config import read_json, write_json


class WebConfig:
    manual_config = "./config/web.json"

    def __init__(self, is_client=False):
        self.config = read_json(self.manual_config, is_client)
        self.is_client = is_client

    def fetch_programs(self):
        return self.config["games"]

    def update_config(self, new_config):
        self.config["games"] = new_config
        write_json(self.manual_config, self.config, self.is_client)

    def fetch_browser(self):
        return self.config["browser"]

    def update_browser(self, new_browser):
        self.config["browser"] = new_browser
        write_json(self.manual_config, self.config, self.is_client)

    def fetch_close_existing(self):
        return self.config["close_existing"]

    def update_close_existing(self, new_close_existing):
        self.config["close_existing"] = new_close_existing
        write_json(self.manual_config, self.config, self.is_client)

    def fetch_kiosk(self):
        return self.config["kiosk"]

    def update_kiosk(self, new_kiosk):
        self.config["kiosk"] = new_kiosk
        write_json(self.manual_config, self.config, self.is_client)

    def fetch_check_ip(self):
        return self.config["check_ip"]

    def update_check_ip(self, new_check_ip):
        self.config["check_ip"] = new_check_ip
        write_json(self.manual_config, self.config, self.is_client)
