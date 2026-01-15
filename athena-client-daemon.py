# You probably do not need this enabled
# This exists solely for people who are turning remote machines on and off
# with start_script and stop_script. You will need to set this up to start for your platform.
import time

from remote.manage import init_client_daemon, parse_state

# Create the daemon indicator for the client
init_client_daemon()

while True:
    parse_state()
    # poll for this file once per minute
    time.sleep(60)
