from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.emulators import EmulatorConfig

bp = Blueprint("emulators", __name__)


@bp.route("/remapping", methods=["GET"])
def fetch_remapping():
    """Fetch emulator remapping configuration"""
    try:
        emulator_config = EmulatorConfig(fetch_client(request))
        return jsonify(emulator_config.fetch_remapping())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/remapping", methods=["POST"])
def update_remapping():
    """Update emulator remapping configuration"""
    try:
        data = request.get_json()
        if not validate(data, "remapping"):
            return validate(data, "remapping")

        emulator_config = EmulatorConfig(fetch_client(request))
        emulator_config.update_remapping(data["remapping"])
        return jsonify({"message": "Remapping updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/selected", methods=["GET"])
def fetch_selected():
    """Fetch selected emulators configuration"""
    try:
        emulator_config = EmulatorConfig(fetch_client(request))
        return jsonify(emulator_config.fetch_selected())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/selected", methods=["POST"])
def update_selected():
    """Update selected emulators configuration"""
    try:
        data = request.get_json()
        if not validate(data, "selected"):
            return validate(data, "selected")

        emulator_config = EmulatorConfig(fetch_client(request))
        emulator_config.update_selected(data["selected"])
        return jsonify({"message": "Selected emulators updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/emulators", methods=["GET"])
def fetch_emulators():
    """Fetch all emulators configuration"""
    try:
        emulator_config = EmulatorConfig(fetch_client(request))
        return jsonify(emulator_config.fetch_emulators())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/emulator/<emulator_name>", methods=["GET"])
def fetch_emulator(emulator_name):
    """Fetch a specific emulator configuration"""
    try:
        emulator_config = EmulatorConfig(fetch_client(request))
        return jsonify(emulator_config.fetch_emulator(emulator_name))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/emulator/<emulator_name>", methods=["POST"])
def update_emulator(emulator_name):
    """Update a specific emulator configuration"""
    try:
        data = request.get_json()
        if not validate(data, "emulator"):
            return validate(data, "emulator")

        emulator_config = EmulatorConfig(fetch_client(request))
        emulator_config.update_emulator(emulator_name, data["emulator"])
        return jsonify({"message": "Emulator updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/emulators", methods=["POST"])
def add_emulator():
    """Add a new emulator configuration"""
    try:
        data = request.get_json()
        if not validate(data, "emulator"):
            return validate(data, "emulator")

        emulator_config = EmulatorConfig(fetch_client(request))
        emulator_config.add_emulator(data["emulator"])
        return jsonify({"message": "Emulator added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
