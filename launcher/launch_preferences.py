from config_lib.athena import AthenaConfigItem
from config_lib.remote import RemoteConfig


# This is parsing the global athena config which is very
# loosely typed, this means we can't use our AthenaConfigItem
# in all places
def merge_based_on_props(current_block, new_block):
    remote_config = RemoteConfig()

    for game in new_block:
        if game not in current_block:
            current_block[game] = new_block[game]
            continue
        local_prefer_local = remote_config.fetch_prefer_local()
        for exception_game in remote_config.fetch_prefer_exceptions():
            if game == exception_game:
                local_prefer_local = not local_prefer_local
                break
        athena_config_item = AthenaConfigItem(current_block[game])
        # Is current config local or not
        if local_prefer_local and athena_config_item.has_script_override():
            continue
        elif local_prefer_local and not athena_config_item.has_script_override():
            current_block[game] = new_block[game]
        elif not local_prefer_local and athena_config_item.has_script_override():
            fallback_script = athena_config_item.script
            current_block[game] = new_block[game]
            current_block[game]["local_script"] = fallback_script
        elif not local_prefer_local and not athena_config_item.has_script_override():
            current_block[game] = new_block[game]
    return current_block
