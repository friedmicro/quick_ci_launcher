from flask import jsonify


def validate(data, key):
    if not data or key not in data:
        return True, jsonify({"error": "Missing " + key}), 400
    else:
        return False
