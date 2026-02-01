from flask import Blueprint, jsonify, request

from api.client import fetch_client
from api.validate import validate
from config_lib.web import WebConfig

bp = Blueprint("web", __name__)


@bp.route("/programs", methods=["GET"])
def fetch_programs():
    """Fetch web programs configuration"""
    try:
        web_config = WebConfig(fetch_client(request))
        return jsonify(web_config.fetch_programs())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/browser", methods=["GET"])
def fetch_browser():
    """Fetch web browser configuration"""
    try:
        web_config = WebConfig(fetch_client(request))
        return jsonify(web_config.fetch_browser())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/close_existing", methods=["GET"])
def fetch_close_existing():
    """Fetch web close_existing configuration"""
    try:
        web_config = WebConfig(fetch_client(request))
        return jsonify(web_config.fetch_close_existing())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/kiosk", methods=["GET"])
def fetch_kiosk():
    """Fetch web kiosk configuration"""
    try:
        web_config = WebConfig(fetch_client(request))
        return jsonify(web_config.fetch_kiosk())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/check_ip", methods=["GET"])
def fetch_check_ip():
    """Fetch web check_ip configuration"""
    try:
        web_config = WebConfig(fetch_client(request))
        return jsonify(web_config.fetch_check_ip())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/config", methods=["POST"])
def update_config():
    """Update web config configuration"""
    try:
        data = request.get_json()
        if not validate(data, "new_config"):
            return validate(data, "new_config")

        web_config = WebConfig(fetch_client(request))
        web_config.update_config(data["new_config"])
        return jsonify({"message": "Config updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/browser", methods=["POST"])
def update_browser():
    """Update web browser configuration"""
    try:
        data = request.get_json()

        if not validate(data, "new_browser"):
            return validate(data, "new_browser")

        web_config = WebConfig(fetch_client(request))
        web_config.update_browser(data["new_browser"])
        return jsonify({"message": "Browser updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/close_existing", methods=["POST"])
def update_close_existing():
    """Update web close_existing configuration"""
    try:
        data = request.get_json()

        if not validate(data, "new_close_existing"):
            return validate(data, "new_close_existing")

        web_config = WebConfig(fetch_client(request))
        web_config.update_close_existing(data["new_close_existing"])
        return jsonify({"message": "Close existing updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/kiosk", methods=["POST"])
def update_kiosk():
    """Update web kiosk configuration"""
    try:
        data = request.get_json()

        if not validate(data, "new_kiosk"):
            return validate(data, "new_kiosk")

        web_config = WebConfig(fetch_client(request))
        web_config.update_kiosk(data["new_kiosk"])
        return jsonify({"message": "Kiosk updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/check_ip", methods=["POST"])
def update_check_ip():
    """Update web check_ip configuration"""
    try:
        data = request.get_json()

        if not validate(data, "new_check_ip"):
            return validate(data, "new_check_ip")

        web_config = WebConfig(fetch_client(request))
        web_config.update_check_ip(data["new_check_ip"])
        return jsonify({"message": "Check IP updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
