# TODO: This is a stub to be worked out later

def create_intial_configs():
    print("Assuming this is the first run of athena; creating default configs")

    # Copy defaults to config/
    # Run game scanner to auto-populate everything from local first, this will give the user a menu of options
    # Populate OS in use to local
    # Generate initial daemon credential file

    # We assume the developer will need to populate each config file as desired; utility code to do this
    # will live in config_lib 
    # Of note:
    # Android: Android games, requires the Android APK name and WayDroid installed (Linux only feature)
    # Client: Machine ID and advanced config logic
    # Combiner: To define partial configs which merge at build, typically used for overrides and automation
    # Emulators: Various emulation options, a user will likely need to configure these as they can be everywhere
    # Manual: This is the baseline for the menu dropdowns, overwriting this lets the user define whatever menu structure they wish
    # Overrides: Currently, this is used to overwrite autodetection of games or to allow users to add games directly to the config.
    # It can also be used to inject into partials in general
    # Remote: Remote machines, typically these are Moonlight machines, this will require the user to install the daemon on the remote
    # Steam: Steam defaults, Linux users may need to change launch commands and other platforms will likely need to change this if they
    # have moved the install location.
    # Time_Config: This is the time management system; it records how long a user has been for example playing games and locks them out.
    # Users who want this feature will need to add a file to serve as a trigger and\or possibly update the config file.
    # Web: This includes web games, specifically forming the commands to run them automatically.
    # Windows_Games: Exclude games\programs when detected, change steam install path, allow opening Steam directly instead of the app when launched