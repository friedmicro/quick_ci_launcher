from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.combiner import CombinerConfig

bp = Blueprint("combiner", __name__)


@bp.route("/time_limit/<config_name>", methods=["GET"])
def get_time_limit(config_name):
    """Get time limit configuration"""
    try:
        combiner_config = CombinerConfig(fetch_client(request))
        return jsonify(combiner_config.get_time_limit(config_name))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_limit/<config_name>", methods=["POST"])
def update_time_limit(config_name):
    """Update time limit configuration"""
    try:
        data = request.get_json()
        if validate(data, "time_limit"):
            return validate(data, "time_limit")

        combiner_config = CombinerConfig(fetch_client(request))
        combiner_config.update_time_limit(config_name, data["time_limit"])
        return jsonify({"message": "Time limit updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_exceptions/<config_name>", methods=["GET"])
def fetch_time_exceptions(config_name):
    """Fetch time exceptions configuration"""
    try:
        combiner_config = CombinerConfig(fetch_client(request))
        return jsonify(combiner_config.fetch_time_exceptions(config_name))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_exceptions/<config_name>", methods=["POST"])
def update_time_exceptions(config_name):
    """Update time exceptions configuration"""
    try:
        data = request.get_json()
        if validate(data, "exceptions"):
            return validate(data, "exceptions")

        combiner_config = CombinerConfig(fetch_client(request))
        combiner_config.update_time_exceptions(config_name, data["exceptions"])
        return jsonify({"message": "Time exceptions updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_files/<config_name>", methods=["GET"])
def fetch_time_files(config_name):
    """Fetch time files configuration"""
    try:
        combiner_config = CombinerConfig(fetch_client(request))
        return jsonify(combiner_config.fetch_time_files(config_name))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_files/<config_name>", methods=["POST"])
def update_time_files(config_name):
    """Update time files configuration"""
    try:
        data = request.get_json()

        if validate(data, "files"):
            return validate(data, "files")

        combiner_config = CombinerConfig(fetch_client(request))
        combiner_config.update_time_files(config_name, data["files"])
        return jsonify({"message": "Time files updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_schedule/<config_name>", methods=["GET"])
def fetch_time_schedule(config_name):
    """Fetch time schedule configuration"""
    try:
        combiner_config = CombinerConfig(fetch_client(request))
        return jsonify(combiner_config.fetch_time_schedule(config_name))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/time_schedule/<config_name>", methods=["POST"])
def update_time_schedule(config_name):
    """Update time schedule configuration"""
    try:
        data = request.get_json()
        if validate(data, "schedule"):
            return validate(data, "schedule")

        combiner_config = CombinerConfig(fetch_client(request))
        combiner_config.update_time_schedule(config_name, data["schedule"])
        return jsonify({"message": "Time schedule updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/files", methods=["GET"])
def fetch_files():
    """Fetch files configuration"""
    try:
        combiner_config = CombinerConfig(fetch_client(request))
        return jsonify(combiner_config.fetch_files())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/files", methods=["POST"])
def add_file():
    """Add file configuration"""
    try:
        data = request.get_json()
        if validate(data, "file"):
            return validate(data, "file")

        combiner_config = CombinerConfig(fetch_client(request))
        combiner_config.add_combiner_file(data["file"])
        return jsonify({"message": "File added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
