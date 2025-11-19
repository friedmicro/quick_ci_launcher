import os

def write(script_name, script_template, folder = "local"):
    file_path = "./scripts/generated_" + folder + "/" + script_name
    f = open(file_path, "w")
    f.write(script_template)
    f.close()
    os.chmod(file_path, 0o775)
    file_path = file_path.replace("generated_" + folder, "dist/" + folder)
    return file_path