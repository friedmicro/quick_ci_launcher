# Parse operation specific parameters
import json


def parse_params(params, argument_is_json, param_count=1):
    operation = params[0]
    arguments = ""
    is_client = False
    if len(params) >= 2:
        if argument_is_json:
            arguments = json.loads(params[1])
        else:
            if param_count > 1:
                arguments = params[1 : 1 + param_count]
            else:
                arguments = params[1]
        if len(params) == 3:
            is_client = bool(params[2])
        else:
            is_client = False
    return operation, arguments, is_client
