from flask import Blueprint, jsonify, request

from config_lib.athena import AthenaConfig

bp = Blueprint("athena", __name__)


@bp.route("/config", methods=["GET"])
def fetch_config():
    """Fetch athena configuration"""
    try:
        athena_config = AthenaConfig()
        return jsonify(athena_config.fetch_config())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
