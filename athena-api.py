from flask import Flask, jsonify, request

# Import UUID authentication
from api.auth import require_uuid_auth
from config_lib.athena import AthenaConfig

# Import blueprints
from config_rest import (
    android,
    athena,
    client,
    combiner,
    emulators,
    local,
    manual,
    overrides,
    remote,
    steam,
    web,
    windows_games,
)
from launcher.exec import headless_start, headless_stop

app = Flask(__name__)

# Register blueprints
app.register_blueprint(android.bp)
app.register_blueprint(athena.bp)
app.register_blueprint(client.bp)
app.register_blueprint(combiner.bp)
app.register_blueprint(emulators.bp)
app.register_blueprint(local.bp)
app.register_blueprint(manual.bp)
app.register_blueprint(overrides.bp)
app.register_blueprint(remote.bp)
app.register_blueprint(steam.bp)
app.register_blueprint(web.bp)
app.register_blueprint(windows_games.bp)


@app.route("/")
def index():
    return jsonify(
        {
            "status": "Athena API is running",
            "endpoints": "/api/<domain>/<operation>",
        }
    )


@app.route("/api/config/<domain>/<operation>", methods=["GET", "POST"])
@require_uuid_auth()
def handle_config(domain, operation):
    try:
        match domain:
            case "android":
                return getattr(android, operation)()
            case "athena":
                return getattr(athena, operation)()
            case "client":
                return getattr(client, operation)()
            case "combiner":
                return getattr(combiner, operation)()
            case "emulators":
                return getattr(emulators, operation)()
            case "local":
                return getattr(local, operation)()
            case "manual":
                return getattr(manual, operation)()
            case "overrides":
                return getattr(overrides, operation)()
            case "remote":
                return getattr(remote, operation)()
            case "steam":
                return getattr(steam, operation)()
            case "web":
                return getattr(web, operation)()
            case "windows_games":
                return getattr(windows_games, operation)()
            case _:
                return jsonify({"error": "Invalid config type"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/exec/<operation>", methods=["POST"])
@require_uuid_auth()
def handle_exec(operation):
    try:
        data = request.get_json()
        match operation:
            case "start":
                headless_start(data["selected_item"])
                return jsonify({"message": "Started successfully"}), 200
            case "stop":
                headless_stop(data["selected_item"])
                return jsonify({"message": "Stopped successfully"}), 200
            case _:
                return jsonify({"error": "Invalid operation"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/list", methods=["GET"])
def handle_list():
    return jsonify({"apps": AthenaConfig().fetch_config()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
