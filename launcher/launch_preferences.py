from scanners.lib.config import read_json

def merge_based_on_props(current_block, new_block):
    remote_config = read_json("./config/remote.json")
    global_prefer_local = remote_config["prefer_local"]
    # Negate whatever is above here
    prefer_exceptions = remote_config["prefer_exceptions"]

    for game in new_block:
        if game not in current_block:
            current_block[game] = new_block[game]
            continue
        local_prefer_local = global_prefer_local
        for exception_game in prefer_exceptions:
            if game == exception_game:
                local_prefer_local = not local_prefer_local
                break
        # Is current config local or not
        current_block_local = current_block[game]["script"] != ""
        if local_prefer_local and current_block_local:
            continue
        elif local_prefer_local and not current_block_local:
            current_block[game] = new_block[game]
        elif not local_prefer_local and current_block_local:
            fallback_script = current_block[game]["script"]
            current_block[game] = new_block[game]
            current_block[game]["local_script"] = fallback_script
        elif not local_prefer_local and not current_block_local:
            current_block[game] = new_block[game]
    return current_block