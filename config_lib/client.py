from lib.config import read_json, write_json

# Note: local overrides are excluded here as they should never be exposed in
# gui interface. Power users may update at their leisure
#
# Custom binaries are also not exposed here, it is unlikely a user will
# want to replace an entire utility binary, if they do as part of dev
# they can update the JSON file. This is for developers mostly.


class GeneratorConfig(dict):
    def __init__(self) -> None:
        generator_config = ClientConfig().fetch_generator()
        self.keep_temp = generator_config["keep_temp"]
        self.scanner_enabled = generator_config["scanner_enabled"]
        self.partials_enabled = generator_config["partials_enabled"]
        self.scanner_path = generator_config["scanner_path"]
        self.combine_partials_path = generator_config["combine_partials_path"]
        self.combine_path = generator_config["combine_path"]
        self.python = generator_config["python"]
        self.node = generator_config["node"]
        dictionary_map = {
            "keep_temp": self.keep_temp,
            "scanner_enabled": self.scanner_enabled,
            "partials_enabled": self.partials_enabled,
            "scanner_path": self.scanner_path,
            "combine_partials_path": self.combine_partials_path,
            "combine_path": self.combine_path,
            "python": self.python,
            "node": self.node,
        }
        super().__init__(self, **dictionary_map)

    # Do not call this unless you are writing back the config file
    def update_hidden_config(self):
        generator_config = ClientConfig().fetch_generator()
        self.scanner_path = generator_config["scanner_path"]
        self.combine_partials_path = generator_config["combine_partials_path"]
        self.combine_path = generator_config["combine_path"]


class ClientConfig:
    manual_config_path = "./config/client.json"

    def __init__(self) -> None:
        pass

    def fetch_id(self):
        return read_json(self.manual_config_path)["id"]

    def update_id(self, new_id):
        current_config = read_json(self.manual_config_path)
        current_config["id"] = new_id
        write_json(self.manual_config_path, current_config)

    def fetch_generator(self):
        return read_json(self.manual_config_path)["generator"]

    def update_generator(self, gen_config: GeneratorConfig):
        full_client_config = read_json(self.manual_config_path)
        gen_config.update_hidden_config()
        full_client_config["generator"] = gen_config
        write_json(self.manual_config_path, full_client_config)
