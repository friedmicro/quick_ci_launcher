from flask import Blueprint, jsonify, request

from api.client import fetch_client
from config_lib.remote import RemoteConfig

bp = Blueprint("remote", __name__)


@bp.route("/hosts", methods=["GET"])
def fetch_hosts():
    """Fetch all remote hosts configuration"""
    try:
        remote_config = RemoteConfig(fetch_client(request))
        return jsonify(remote_config.fetch_hosts())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/hosts", methods=["POST"])
def add_host():
    """Add a new remote host"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.add_host(data["host_name"], data["host_config"])
        return jsonify({"message": "Host added successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/hosts/<host_name>", methods=["POST"])
def update_host(host_name):
    """Update an existing remote host"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.update_host(host_name, data["host_config"])
        return jsonify({"message": "Host updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/scan_options", methods=["GET"])
def fetch_scan_options():
    """Fetch scan options configuration"""
    try:
        remote_config = RemoteConfig(fetch_client(request))
        return jsonify(remote_config.fetch_scan_options())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/scan_options", methods=["POST"])
def update_scan_options():
    """Update scan options configuration"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.update_scan_options(data["scan_options"])
        return jsonify({"message": "Scan options updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/remotes_to_load", methods=["GET"])
def fetch_remotes_to_load():
    """Fetch remotes to load configuration"""
    try:
        remote_config = RemoteConfig(fetch_client(request))
        return jsonify(remote_config.fetch_remotes_to_load())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/remotes_to_load", methods=["POST"])
def update_remotes_to_load():
    """Update remotes to load configuration"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.update_remotes_to_load(data["remotes_to_load"])
        return jsonify({"message": "Remotes to load updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/defaults", methods=["GET"])
def fetch_defaults():
    """Fetch defaults configuration"""
    try:
        remote_config = RemoteConfig(fetch_client(request))
        return jsonify(remote_config.fetch_defaults())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/defaults", methods=["POST"])
def update_defaults():
    """Update defaults configuration"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.update_defaults(data["defaults"])
        return jsonify({"message": "Defaults updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/prefer_local", methods=["GET"])
def fetch_prefer_local():
    """Fetch prefer_local configuration"""
    try:
        remote_config = RemoteConfig(fetch_client(request))
        return jsonify(remote_config.fetch_prefer_local())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/prefer_local", methods=["POST"])
def update_prefer_local():
    """Update prefer_local configuration"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.update_prefer_local(data["prefer_local"])
        return jsonify({"message": "Prefer local updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/prefer_exceptions", methods=["GET"])
def fetch_prefer_exceptions():
    """Fetch prefer_exceptions configuration"""
    try:
        remote_config = RemoteConfig(fetch_client(request))
        return jsonify(remote_config.fetch_prefer_exceptions())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/prefer_exceptions", methods=["POST"])
def update_prefer_exceptions():
    """Update prefer_exceptions configuration"""
    try:
        data = request.get_json()
        remote_config = RemoteConfig(fetch_client(request))
        remote_config.update_prefer_exceptions(data["prefer_exceptions"])
        return jsonify({"message": "Prefer exceptions updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
