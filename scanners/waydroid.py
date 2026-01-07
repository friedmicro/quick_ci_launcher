from config_lib.android import AndroidConfig


def generate_waydroid():
    return AndroidConfig().load_config_map()
