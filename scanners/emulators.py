import os

from config_lib.athena import AthenaConfig
from config_lib.emulators import EmulatorConfig


def parse_roms():
    emulators_config = EmulatorConfig()
    rom_jsons = {}

    athena_config = AthenaConfig()
    for emulator in emulators_config.fetch_emulators():
        emulator_config = emulators_config.fetch_emulator(emulator)
        for item in os.listdir(emulator_config.paths):
            if emulator_config.is_single_file:
                rom_type = item.split(".")[-1]
            else:
                for child_item in os.listdir(emulator_config.paths + "/" + item):
                    if child_item.split(".")[-1] in emulator_config.extensions:
                        rom_type = child_item.split(".")[-1]
                        rom_file_name = child_item
            if rom_type in emulator_config.extensions:
                if not (emulator_config.scan or item in emulators_config.selected):
                    continue
                if not emulator_config.is_single_file:
                    file_path = emulator_config.paths + "/" + item + "/" + rom_file_name
                else:
                    file_path = emulator_config.paths + "/" + item
                seperator = emulator_config.truncate_sequence
                if seperator != "":
                    item = item.split(emulator_config.truncate_sequence)[0]
                if item in emulators_config.remapping:
                    item = emulators_config.remapping[item]
                rom_jsons[item] = athena_config.generate_emulator(file_path, emulator)

    return rom_jsons
