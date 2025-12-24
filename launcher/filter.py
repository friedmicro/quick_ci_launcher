import subprocess

from launcher.lib.remote import ping_ip


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
        if "local_script" in menu_topology["Games"][game]:
            games[game] = menu_topology["Games"][game]
        elif "layer" in menu_topology["Games"][game]:
            if menu_topology["Games"][game]["layer"] == "waydroid" and waydroid_not_installed:
                continue
        elif "ip" in menu_topology["Games"][game]:
            live_ip = menu_topology["Games"][game]["live_check"]
            if live_ip in ips_offline:
                continue
            if live_ip not in ips_online:
                if ping_ip(live_ip):
                    ips_online.append(live_ip)
                else:
                    ips_offline.append(live_ip)
                    continue
            games[game] = menu_topology["Games"][game]
        else:
            games[game] = menu_topology["Games"][game]
    menu_topology["Games"] = games
    return menu_topology
