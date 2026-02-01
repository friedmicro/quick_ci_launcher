from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.windows_games import WindowsGamesConfig

bp = Blueprint("windows_games", __name__)


@bp.route("/exclude", methods=["GET"])
def fetch_exclude():
    """Fetch windows_games exclude configuration"""
    try:
        windows_games_config = WindowsGamesConfig(fetch_client(request))
        return jsonify(windows_games_config.fetch_exclude())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/exclude", methods=["POST"])
def update_exclude():
    """Update windows_games exclude configuration"""
    try:
        data = request.get_json()

        if not validate(data, "exclude"):
            return validate(data, "exclude")

        windows_games_config = WindowsGamesConfig(fetch_client(request))
        windows_games_config.update_exclude(data["exclude"])
        return jsonify({"message": "Exclude updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/open_steam_direct", methods=["GET"])
def fetch_open_steam_direct():
    """Fetch open steam direct configuration"""
    try:
        windows_games_config = WindowsGamesConfig(fetch_client(request))
        return jsonify(windows_games_config.fetch_open_steam_direct())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/open_steam_direct", methods=["POST"])
def update_open_steam_direct():
    """Update open steam direct configuration"""
    try:
        data = request.get_json()

        if not validate(data, "open_steam_direct"):
            return validate(data, "open_steam_direct")

        windows_games_config = WindowsGamesConfig(fetch_client(request))
        windows_games_config.update_open_steam_direct(data["open_steam_direct"])
        return jsonify({"message": "Open steam direct updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/steam_path", methods=["GET"])
def fetch_steam_path():
    """Fetch steam path configuration"""
    try:
        windows_games_config = WindowsGamesConfig(fetch_client(request))
        return jsonify(windows_games_config.fetch_steam_path())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/steam_path", methods=["POST"])
def update_steam_path():
    """Update steam path configuration"""
    try:
        data = request.get_json()
        if not validate(data, "steam_path"):
            return validate(data, "steam_path")

        windows_games_config = WindowsGamesConfig(fetch_client(request))
        windows_games_config.update_steam_path(data["steam_path"])
        return jsonify({"message": "Steam path updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
