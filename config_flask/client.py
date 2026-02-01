from flask import Blueprint, jsonify, request

from api.validate import validate
from config_lib.client import ClientConfig

bp = Blueprint("client", __name__)


@bp.route("/id", methods=["GET"])
def fetch_id():
    """Fetch client ID"""
    try:
        client_config = ClientConfig()
        return jsonify(client_config.fetch_id())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/id", methods=["POST"])
def update_id():
    """Update client ID"""
    try:
        data = request.get_json()
        if not validate(data, "id"):
            return validate(data, "id")

        client_config = ClientConfig()
        client_config.update_id(data["id"])
        return jsonify({"message": "Client ID updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/generator", methods=["GET"])
def fetch_generator():
    """Fetch generator configuration"""
    try:
        client_config = ClientConfig()
        return jsonify(client_config.fetch_generator())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/generator", methods=["POST"])
def update_generator():
    """Update generator configuration"""
    try:
        data = request.get_json()
        if not validate(data, "generator"):
            return validate(data, "generator")

        client_config = ClientConfig()
        client_config.update_generator(data["generator"])
        return jsonify({"message": "Generator updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
