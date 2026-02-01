from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.local import LocalConfig

bp = Blueprint("local", __name__)


@bp.route("/local", methods=["GET"])
def fetch_local():
    """Fetch local configuration"""
    try:
        local_config = LocalConfig(fetch_client(request))
        return jsonify(local_config.fetch_local())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/local", methods=["POST"])
def update_local():
    """Update local configuration"""
    try:
        data = request.get_json()
        if not validate(data, "local"):
            return validate(data, "local")

        local_config = LocalConfig(fetch_client(request))
        local_config.update_local(data["local"])
        return jsonify({"message": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
