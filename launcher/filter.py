from launcher.lib.remote import ping_ip


# For now this only supports games, we can assume enterprise\productivity
# usecases want these to always show.
def clear_out_of_scope(menu_topology):
    games = {}
    ips_online = []
    ips_offline = []
    for game in menu_topology["Games"]:
        if "ip" in menu_topology["Games"][game]:
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
