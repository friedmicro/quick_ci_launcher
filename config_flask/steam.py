from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.steam import SteamConfig

bp = Blueprint("steam", __name__)


@bp.route("/remapping", methods=["GET"])
def fetch_remapping():
    """Fetch steam remapping configuration"""
    try:
        steam_config = SteamConfig(fetch_client(request))
        return jsonify(steam_config.fetch_remapping())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/remapping", methods=["POST"])
def update_remapping():
    """Update steam remapping configuration"""
    try:
        data = request.get_json()
        if not validate(data, "remapping"):
            return validate(data, "remapping")

        steam_config = SteamConfig(fetch_client(request))
        steam_config.update_remapping(data["remapping"])
        return jsonify({"status": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/exclude", methods=["GET"])
def fetch_exclude():
    """Fetch steam exclude configuration"""
    try:
        steam_config = SteamConfig(fetch_client(request))
        return jsonify(steam_config.fetch_exclude())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/exclude", methods=["POST"])
def update_exclude():
    """Update steam exclude configuration"""
    try:
        data = request.get_json()
        if not validate(data, "exclude"):
            return validate(data, "exclude")

        steam_config = SteamConfig(fetch_client(request))
        steam_config.update_exclude(data["exclude"])
        return jsonify({"status": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/host/<host>", methods=["GET"])
def fetch_host(host):
    """Fetch steam host configuration"""
    try:
        steam_config = SteamConfig(fetch_client(request))
        return jsonify(steam_config.fetch_host(host))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/host/<host>", methods=["POST"])
def update_host(host):
    """Update steam host configuration"""
    try:
        data = request.get_json()
        if not validate(data, "host"):
            return validate(data, "host")

        steam_config = SteamConfig(fetch_client(request))
        steam_config.update_host(host, data["host"])
        return jsonify({"status": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
