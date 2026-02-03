import subprocess

from config_lib.athena import AthenaConfigItem
from lib.remote import ping_ip


# For now this only supports games, we can assume enterprise\productivity
# usecases want these to always show.
def clear_out_of_scope(menu_topology):
    games = {}
    ips_online = []
    ips_offline = []

    # If waydroid is not installed; skip, this is so that we don't have to worry about this showing up
    # on unsopported machines
    result = subprocess.run(["which", "waydroid"], stderr=subprocess.STDOUT, timeout=1)
    waydroid_not_installed = result.returncode != 0

    for game in menu_topology["Games"]:
        athena_item = AthenaConfigItem(menu_topology["Games"][game])
        if athena_item.is_hidden():
            continue
        elif athena_item.has_local_script():
            games[game] = menu_topology["Games"][game]
        elif athena_item.is_layer():
            if athena_item.is_waydroid() and waydroid_not_installed:
                continue
            games[game] = menu_topology["Games"][game]
        elif athena_item.has_ip():
            if athena_item.live_check in ips_offline:
                continue
            if athena_item.live_check not in ips_online:
                if ping_ip(athena_item.live_check):
                    ips_online.append(athena_item.live_check)
                else:
                    ips_offline.append(athena_item.live_check)
                    continue
            games[game] = menu_topology["Games"][game]
        else:
            games[game] = menu_topology["Games"][game]
    menu_topology["Games"] = games
    return menu_topology
