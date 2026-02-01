from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.android import AndroidConfig

bp = Blueprint("android", __name__)


@bp.route("/load_apps", methods=["GET"])
def load_apps():
    """Load Android apps configuration"""
    try:
        android_config = AndroidConfig(fetch_client(request))
        return jsonify(android_config.load_apps())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/config", methods=["POST"])
def update_config():
    """Update Android configuration"""
    try:
        data = request.get_json()
        if not validate(data, "config"):
            return validate(data, "config")

        android_config = AndroidConfig(fetch_client(request))
        android_config.update_config(data["config"])
        return jsonify({"status": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
