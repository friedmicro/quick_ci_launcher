from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.overrides import OverridesConfig

bp = Blueprint("overrides", __name__)


@bp.route("/overrides", methods=["GET"])
def fetch_overrides():
    """Fetch overrides configuration"""
    try:
        overrides_config = OverridesConfig(fetch_client(request))
        return jsonify(overrides_config.fetch_overrides())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/overrides", methods=["POST"])
def update_overrides():
    """Update overrides configuration"""
    try:
        data = request.get_json()
        if not validate(data, "overrides"):
            return validate(data, "overrides")

        overrides_config = OverridesConfig(fetch_client(request))
        overrides_config.update_overrides(data["overrides"])
        return jsonify({"message": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
