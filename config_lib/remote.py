from lib.config import read_json, write_json


class RemoteHostConfig(dict):
    def __init__(self, config_data):
        self.os = config_data["os"]
        self.ip = config_data["ip"]
        self.live_check = config_data["live_check"]
        self.remote_client_type = config_data["remote_client_type"]
        dictionary_map = {
            "os": self.os,
            "ip": self.ip,
            "live_check": self.live_check,
            "remote_client_type": self.remote_client_type,
        }
        if self.remote_client_type == "moonlight":
            self.moonlight_app = config_data["moonlight_app"]
            self.moonlight_machine = config_data["moonlight_machine"]
            dictionary_map.update(
                {
                    "moonlight_app": self.moonlight_app,
                    "moonlight_machine": self.moonlight_machine,
                }
            )
        if "start_script" in config_data:
            self.start_script = config_data["start_script"]
            dictionary_map["start_script"] = self.start_script
        if "stop_script" in config_data:
            self.stop_script = config_data["stop_script"]
            dictionary_map["stop_script"] = self.stop_script
        if "manual" in config_data:
            self.manual = config_data["manual"]
            dictionary_map["manual"] = self.manual
        if "skip_assets" in config_data:
            skip_assets = config_data["skip_assets"]
        else:
            skip_assets = False
        self.skip_assets = skip_assets
        dictionary_map["skip_assets"] = skip_assets
        if "athena_installed" in config_data:
            athena_installed = config_data["athena_installed"]
        else:
            athena_installed = True
        self.athena_installed = athena_installed
        dictionary_map["athena_installed"] = athena_installed
        if "skip_stop_command" in config_data:
            skip_stop_command = config_data["skip_stop_command"]
        else:
            skip_stop_command = False
        self.skip_stop_command = skip_stop_command
        dictionary_map["skip_stop_command"] = skip_stop_command
        if "user" in config_data:
            self.user = config_data["user"]
            dictionary_map["user"] = self.user
        super().__init__(self, **dictionary_map)


class RemoteConfig:
    manual_config_path = "./config/remote.json"

    def __init__(self, is_client=False) -> None:
        self.config_data = read_json(self.manual_config_path, is_client)
        self.is_client = is_client
        pass

    def fetch_hosts(self):
        hosts = self.config_data["hosts"]
        host_configs = {}
        for host in hosts:
            host_configs[host] = RemoteHostConfig(self.config_data[host])
        return host_configs

    def add_host(self, host_name, host_config):
        self.config_data["hosts"].append(host_name)
        self.config_data[host_name] = host_config
        write_json(self.manual_config_path, self.config_data, self.is_client)

    def update_host(self, host_name, host_config):
        self.config_data[host_name] = host_config
        write_json(self.manual_config_path, self.config_data, self.is_client)

    def fetch_scan_options(self):
        scan_options = self.config_data["scan_options"]
        return scan_options

    def update_scan_options(self, scan_options):
        self.config_data["scan_options"] = scan_options
        write_json(self.manual_config_path, self.config_data, self.is_client)

    def fetch_remotes_to_load(self):
        remotes_to_load = self.config_data["remotes_to_load"]
        return remotes_to_load

    def update_remotes_to_load(self, remotes_to_load):
        self.config_data["remotes_to_load"] = remotes_to_load
        write_json(self.manual_config_path, self.config_data, self.is_client)

    def fetch_defaults(self):
        defaults = self.config_data["defaults"]
        return defaults

    def update_defaults(self, defaults):
        self.config_data["defaults"] = defaults
        write_json(self.manual_config_path, self.config_data, self.is_client)

    def fetch_prefer_local(self):
        prefer_local = self.config_data["prefer_local"]
        return prefer_local

    def update_prefer_local(self, prefer_local):
        self.config_data["prefer_local"] = prefer_local
        write_json(self.manual_config_path, self.config_data, self.is_client)

    def fetch_prefer_exceptions(self):
        prefer_exceptions = self.config_data["prefer_exceptions"]
        return prefer_exceptions

    def update_prefer_exceptions(self, prefer_exceptions):
        self.config_data["prefer_exceptions"] = prefer_exceptions
        write_json(self.manual_config_path, self.config_data, self.is_client)
