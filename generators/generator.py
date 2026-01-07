# This file is here to generate the athena config
# This is preferable over a shell script due to the complexity and because we want to
# have support across multiple OSes, this binary will run when a user wants to update the athena
# config
import os
import shutil
import subprocess

from config_lib.client import ClientConfig, GeneratorConfig
from config_lib.manual import ManualConfig
from lib.os import copy_all_contents, get_os_delimiter, mkdirp

# Scripts may not exist if the user has not definted any manual folders
if not os.path.exists("./scripts"):
    os.mkdir("./scripts")
    # Let's also create the manual folders to save some work for the user
    os.mkdir("./scripts/manual_local")
    os.mkdir("./scripts/manual_remote")

# Purge the existing scripts; dist is the final directory
shutil.rmtree("./scripts/dist/local", ignore_errors=True)
shutil.rmtree("./scripts/dist/remote", ignore_errors=True)
shutil.rmtree("./scripts/dist/assets", ignore_errors=True)

# Generate script directories and generator temps
mkdirp("./scripts/generated_local")
mkdirp("./scripts/generated_remote")
mkdirp("./scripts/dist")
mkdirp("./scripts/dist/local")
mkdirp("./scripts/dist/remote")
mkdirp("./scripts/dist/assets")
mkdirp("./generators/out")

client_config = ClientConfig()
generator_config = GeneratorConfig()

# We use the manual.json as the existing basis for the config
ManualConfig().copy_config(client_config.fetch_id())

# Hot-plugged generators, these can by in python, js, or in any compiled binary
generator_plugin_path = "./generators/types"
delimiter = get_os_delimiter()
for filename in os.listdir(generator_plugin_path):
    exec_path = generator_plugin_path + delimiter + filename
    # Internal library is always in this folder, skip
    if filename == "lib":
        continue
    elif ".py" in filename:
        subprocess.run([generator_config.python + " " + exec_path], shell=True)
    elif ".js" in filename:
        subprocess.run([generator_config.node + " " + exec_path], shell=True)
    else:
        subprocess.run([generator_plugin_path + delimiter + filename], shell=True)

# Athena binaries
# Scanner: Search for new entries
if generator_config.scanner_enabled:
    subprocess.run([generator_config.scanner_path])
if generator_config.partials_enabled:
    # Partials: combine partial json configs from a user
    subprocess.run([generator_config.combine_partials_path])
    subprocess.run([generator_config.combine_path])

# Copy generated files
copy_all_contents("./scripts/generated_local", "./scripts/dist/local", True)
copy_all_contents("./scripts/manual_local", "./scripts/dist/local", True)
copy_all_contents("./scripts/generated_remote", "./scripts/dist/remote", True)
copy_all_contents("./scripts/manual_remote", "./scripts/dist/remote", True)
copy_all_contents("./scripts/assets", "./scripts/dist/assets", True)

# If configured cleanup old files
if not generator_config["keep_temp"]:
    shutil.rmtree("./scripts/generated_local", ignore_errors=True)
    shutil.rmtree("./scripts/generated_remote", ignore_errors=True)
    shutil.rmtree("./generators/out", ignore_errors=True)

if "after_hook" in generator_config:
    subprocess.run([generator_config.after_hook], shell=True)
