import os

from scanners.lib.config import read_json


def parse_roms():
    emulator_config = read_json("./config/emulators.json")
    rom_jsons = {}

    for emulator in emulator_config["registered_emulators"]:
        rom_path = emulator_config["paths"][emulator]
        scanning_enabled = emulator_config["scan"][emulator]
        selected_roms = emulator_config["selected"]
        for item in os.listdir(rom_path):
            if emulator_config["is_single_file"][emulator]:
                rom_type = item.split(".")[-1]
            else:
                for child_item in os.listdir(rom_path + "/" + item):
                    if (
                        child_item.split(".")[-1]
                        in emulator_config["extensions"][emulator]
                    ):
                        rom_type = child_item.split(".")[-1]
                        rom_file_name = child_item
            if rom_type in emulator_config["extensions"][emulator]:
                if not (scanning_enabled or item in selected_roms):
                    continue
                if not emulator_config["is_single_file"][emulator]:
                    file_path = (
                        emulator_config["paths"][emulator]
                        + "/"
                        + item
                        + "/"
                        + rom_file_name
                    )
                else:
                    file_path = emulator_config["paths"][emulator] + "/" + item
                seperator = emulator_config["truncate_sequence"][emulator]
                if seperator != "":
                    item = item.split(emulator_config["truncate_sequence"][emulator])[0]
                if item in emulator_config["remapping"]:
                    item = emulator_config["remapping"][item]
                rom_jsons[item] = {
                    "asset": file_path,
                    "emulator": emulator,
                    "script": "",
                }

    return rom_jsons
