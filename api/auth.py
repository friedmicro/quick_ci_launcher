from functools import wraps
from typing import List, Optional

from flask import jsonify, request

from lib.config import read_json


class UUIDAuthMiddleware:
    """
    UUID-based authentication middleware for Flask API.
    Valid UUIDs can be loaded from a configuration file or hardcoded.
    """

    def __init__(self):
        """Initialize the auth middleware with valid UUIDs."""
        self.valid_uuids = self._load_valid_uuids()

    def _load_valid_uuids(self) -> List[str]:
        """
        Load valid UUIDs from configuration.
        """
        config = read_json("./config/api_auth_config.json")
        valid_uuids = config["valid_uuids"]
        return valid_uuids

    def is_valid_uuid(self, uuid_str: str) -> bool:
        """Check if a UUID string is whitelisted."""
        return uuid_str in self.valid_uuids

    def get_auth_header(self) -> Optional[str]:
        """Extract the Authorization header from the request."""
        auth_header = request.headers.get("Authorization", "")

        # Expected format: "Bearer <uuid>"
        if auth_header.startswith("Bearer "):
            return auth_header[7:].strip()
        return None

    def require_uuid_auth(self):
        """
        Decorator factory that creates a decorator requiring UUID authentication.
        Usage:
            @uuid_auth.require_uuid_auth()
            def protected_route():
                ...
        """

        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                uuid_str = self.get_auth_header()

                if not uuid_str:
                    return jsonify(
                        {
                            "error": "Authentication required",
                            "message": "Authorization header is missing or invalid",
                            "hint": "Use 'Bearer <uuid>' in the Authorization header",
                        }
                    ), 401

                if not self.is_valid_uuid(uuid_str):
                    return jsonify(
                        {
                            "error": "Unauthorized access",
                            "message": "The provided UUID is not authorized",
                        }
                    ), 403

                return f(*args, **kwargs)

            return decorated_function

        return decorator


def require_uuid_auth():
    """Decorator for routes that require UUID authentication."""
    auth = UUIDAuthMiddleware()
    return auth.require_uuid_auth()
