# Steam only officially support Linux, Windows, and MacOS.
# For this reason we're not going to allow adding new hosts here
# if someone wants to add an additional host they can, but this is an
# edge case that does not need added in the GUI or tooling
# technically speaking...the rest of the code will work regardless.
# A valid usecase for this maybe multiple remote game machines running the same OS.
from lib.config import read_json, write_json


class SteamLocation(dict):
    def __init__(self, steam_location_data) -> None:
        self.path = steam_location_data["path"]
        self.mode = steam_location_data["mode"]
        dictionary_map = {
            "path": self.path,
            "mode": self.mode,
        }
        super().__init__(self, **dictionary_map)


class SteamHostConfig(dict):
    def __init__(self, steam_host_data) -> None:
        self.os = steam_host_data["os"]
        self.native = steam_host_data["native"]
        self.locations = []
        for location in steam_host_data["locations"]:
            self.locations.append(SteamLocation(location))
        dictionary_map = {
            "os": self.os,
            "native": self.native,
            "locations": self.locations,
        }
        if "flatpak" in steam_host_data:
            self.flatpak = steam_host_data["flatpak"]
            dictionary_map["flatpak"] = self.flatpak
        super().__init__(self, **dictionary_map)


class SteamConfig:
    manual_config = "./config/steam.json"

    def __init__(self):
        self.config_data = read_json(self.manual_config)

    def fetch_remapping(self):
        return self.config_data["remapping"]

    def update_remapping(self, new_remapping):
        self.config_data["remapping"] = new_remapping
        write_json(self.manual_config, self.config_data)

    def fetch_exclude(self):
        return self.config_data["exclude"]

    def update_exclude(self, new_exclude):
        self.config_data["exclude"] = new_exclude
        write_json(self.manual_config, self.config_data)

    def fetch_host(self, host):
        # Let's trust that the user will not directly
        # access a key they shouldn't.
        item = SteamHostConfig(self.config_data[host])
        return item

    def update_host(self, host, new_host):
        self.config_data[host] = new_host
        write_json(self.manual_config, self.config_data)
