import platform
import subprocess


def ping_ip(host):
    param = "-n" if "win" in platform.system().lower() else "-c"
    command = ["ping", param, "1", host]
    try:
        result = subprocess.run(command, stderr=subprocess.STDOUT, timeout=1)
        return result.returncode == 0
    except:
        return False
