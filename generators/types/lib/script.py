import os


def write(script_name, script_template, folder="local"):
    file_path = get_script_path(script_name, folder)[1]
    f = open(file_path, "w")
    f.write(script_template)
    f.close()
    os.chmod(file_path, 0o775)
    file_path = get_script_path(script_name, folder)[0]
    return file_path


def get_script_path(script_name, folder="local"):
    dist_path = "./scripts/dist/" + folder + "/" + script_name
    generated_path = "./scripts/generated_" + folder + "/" + script_name
    return dist_path, generated_path
