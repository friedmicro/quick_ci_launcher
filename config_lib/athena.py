# This serves as the basis for all configuration objects\templating
# It does not allow modification to the config.json object by design
# It is highly encouraged to not mutate the config here

from config_lib.remote import RemoteConfig
from lib.config import read_json


class AthenaConfigItem(dict):
    def __init__(self, config_data):
        dictionary_map = {}
        self.parse_partials(config_data, dictionary_map)
        self.parse_layers(config_data, dictionary_map)
        self.parse_common(config_data, dictionary_map)
        self.parse_emulator(config_data, dictionary_map)
        self.parse_web(config_data, dictionary_map)
        self.parse_remote(config_data, dictionary_map)
        self.parse_local_installs(config_data, dictionary_map)
        self.parse_ui_props(config_data, dictionary_map)
        super().__init__(self, **dictionary_map)

    def parse_partials(self, config_data, dictionary_map):
        if "partial" in config_data:
            self.partial = config_data["partial"]
            dictionary_map["partial"] = self.partial

    def parse_layers(self, config_data, dictionary_map):
        if "layer" in config_data:
            self.layer = config_data["layer"]
            dictionary_map["layer"] = self.layer

    def parse_common(self, config_data, dictionary_map):
        if "script" in config_data:
            self.script = config_data["script"]
            dictionary_map["script"] = self.script
        if "asset" in config_data:
            self.asset = config_data["asset"]
            dictionary_map["asset"] = self.asset
        if "time_limit" in config_data:
            self.time_limit = config_data["time_limit"]
            dictionary_map["time_limit"] = self.time_limit

    def parse_emulator(self, config_data, dictionary_map):
        if "emulator" in config_data:
            self.emulator = config_data["emulator"]
            dictionary_map["emulator"] = self.emulator

    def parse_web(self, config_data, dictionary_map):
        if "web" in config_data:
            self.web = config_data["web"]
            dictionary_map["web"] = self.web

    def parse_remote(self, config_data, dictionary_map):
        if "ip" in config_data:
            self.ip = config_data["ip"]
            self.live_check = config_data["live_check"]
            dictionary_map.update(
                {
                    "ip": self.ip,
                    "live_check": self.live_check,
                }
            )
        if "remote_client_type" in config_data:
            self.remote_client_type = config_data["remote_client_type"]
            self.os = config_data["os"]
            dictionary_map.update(
                {
                    "remote_client_type": self.remote_client_type,
                    "os": self.os,
                }
            )
            if "skip_assets" in config_data:
                skip_assets = config_data["skip_assets"]
            else:
                skip_assets = False
            self.skip_assets = skip_assets
            dictionary_map["skip_assets"] = self.skip_assets
            if "athena_installed" in config_data:
                athena_installed = config_data["athena_installed"]
            else:
                athena_installed = True
            self.athena_installed = athena_installed
            dictionary_map["athena_installed"] = self.athena_installed
        if (
            "remote_client_type" in config_data
            and self.remote_client_type == "moonlight"
        ):
            self.moonlight_app = config_data["moonlight_app"]
            self.moonlight_machine = config_data["moonlight_machine"]
            dictionary_map.update(
                {
                    "moonlight_app": self.moonlight_app,
                    "moonlight_machine": self.moonlight_machine,
                }
            )
        if "remote_client_type" in config_data and self.remote_client_type == "rdp":
            self.user = config_data["user"]
            dictionary_map.update(
                {
                    "user": self.user,
                }
            )
        if "start_script" in config_data:
            self.start_script = config_data["start_script"]
            dictionary_map["start_script"] = self.start_script
        if "stop_script" in config_data:
            self.stop_script = config_data["stop_script"]
            dictionary_map["stop_script"] = self.stop_script
        if "skip_stop_command" in config_data:
            self.skip_stop_command = config_data["skip_stop_command"]
            dictionary_map["skip_stop_command"] = self.skip_stop_command

    def parse_local_installs(self, config_data, dictionary_map):
        if "local_script" in config_data:
            self.local_script = config_data["local_script"]
            dictionary_map["local_script"] = self.local_script

    def parse_ui_props(self, config_data, dictionary_map):
        if "hidden" in config_data:
            self.hidden = config_data["hidden"]
            dictionary_map["hidden"] = self.hidden

    def has_script_override(self):
        return "script" in self and self.script != ""

    def is_partial(self):
        return "partial" in self

    def is_emulator(self):
        return "emulator" in self

    def is_layer(self):
        return "layer" in self

    def is_waydroid(self):
        return self.layer == "waydroid"

    def is_web(self):
        return "web" in self

    def has_ip(self):
        return "ip" in self

    def is_remote(self):
        return "asset" in self

    def has_local_script(self):
        return "local_script" in self

    def has_start_script(self):
        return "start_script" in self and self.start_script != ""

    def has_stop_script(self):
        return "stop_script" in self and self.stop_script != ""

    def is_hidden(self):
        return "hidden" in self and self.hidden


class AthenaConfig:
    def __init__(self) -> None:
        self.__athena_config = read_json("./config.json")
        pass

    def fetch_config(self):
        return self.__athena_config

    def generate_partial(self, file):
        return AthenaConfigItem({"partial": file})

    def generate_script(self, script):
        return AthenaConfigItem({"script": script})

    def generate_waydroid(self, app_name):
        return AthenaConfigItem({"layer": "waydroid", "script": "", "asset": app_name})

    def add_time_limits(self, item, time_status):
        item["time_limit"] = time_status
        return AthenaConfigItem(item)

    def generate_emulator(self, file_path, emulator):
        return AthenaConfigItem(
            {"emulator": emulator, "script": "", "asset": file_path}
        )

    def generate_web(self, url, check_domain):
        return AthenaConfigItem(
            {"script": "", "web": url, "ip": check_domain, "live_check": check_domain}
        )

    def generate_remote(self, asset_path, host):
        item = {"asset": asset_path, "script": ""}
        remote_config = RemoteConfig().fetch_hosts()[host]
        item["ip"] = remote_config.ip
        if "start_script" in remote_config:
            item["start_script"] = remote_config.start_script
        if "stop_script" in remote_config:
            item["stop_script"] = remote_config.stop_script
        item["live_check"] = remote_config.live_check
        if "moonlight_app" in remote_config:
            item["moonlight_app"] = remote_config.moonlight_app
        if "moonlight_machine" in remote_config:
            item["moonlight_machine"] = remote_config.moonlight_machine
        if "user" in remote_config:
            item["user"] = remote_config.user
        if "skip_assets" in remote_config:
            item["skip_assets"] = remote_config.skip_assets
        if "athena_installed" in remote_config:
            item["athena_installed"] = remote_config.athena_installed
        if "skip_stop_command" in remote_config:
            item["skip_stop_command"] = remote_config.skip_stop_command
        item["remote_client_type"] = remote_config.remote_client_type
        item["os"] = remote_config.os
        return AthenaConfigItem(item)
