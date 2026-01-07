import json

from config_lib.combiner import CombinerConfig

combiner_config = CombinerConfig()
combiner_config.merge_partials()
combined_files = combiner_config.files

for combination in combined_files:
    combination_data = combined_files[combination]
    temp_list = combiner_config.process_simple_and_complex_files()

    # Sort by name
    temp_list = sorted(temp_list, key=lambda x: x["name"], reverse=False)
    tmp_json = combiner_config.convert_to_config_map(temp_list, combination_data)

    with open(combination, "w") as outfile:
        outfile.write(json.dumps(tmp_json, indent=4))
