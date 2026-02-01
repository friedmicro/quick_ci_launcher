from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.manual import ManualConfig

bp = Blueprint("manual", __name__)


@bp.route("/data", methods=["GET"])
def fetch_data():
    """Fetch manual configuration data"""
    try:
        manual_config = ManualConfig(fetch_client(request))
        return jsonify(manual_config.fetch_data())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/data/<index>", methods=["POST"])
def update_at_index(index):
    """Update manual configuration at specific index"""
    try:
        data = request.get_json()
        if not validate(data, "data"):
            return validate(data, "data")

        manual_config = ManualConfig(fetch_client(request))
        manual_config.update_at_index(index, data["data"])
        return jsonify({"message": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
