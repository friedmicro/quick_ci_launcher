## Overview

This guide explains how to use the UUID-based authentication middleware for the Athena API.

## Configuration

### Creating Valid UUIDs

Generate UUIDs or any password for that matter:

Store these specific UUIDs in `auth_config.json`:

```json
{
  "valid_uuids": [
    "your-client-uuid-1",
    "your-client-uuid-2",
    "another-client-uuid"
  ]
}
```

## Usage

### Route Protection

Add the `@require_uuid_auth()` decorator to protect routes:

```python
from flask import Blueprint
from api.auth import require_uuid_auth

bp = Blueprint("my_api", __name__)

@bp.route("/protected", methods=["GET"])
@require_uuid_auth()
def protected_route():
    return jsonify({"message": "This is protected!"})
```

## Authentication Formats

Authentication header format supported:

**Bearer token**: `Authorization: Bearer <uuid>`
   ```bash
   curl -H "Authorization: Bearer 123e4567-e89b-12d3-a456-426614174000" http://localhost:5000/api/config/android/load_apps
   ```

## Error Responses

The authentication system returns standardized error responses:

### Missing Authentication
```json
{
  "error": "Authentication required",
  "message": "Authorization header is missing or invalid",
  "hint": "Use 'Bearer <uuid>' in the Authorization header"
}
```
Status: 401 Unauthorized

### Unauthorized Access
```json
{
  "error": "Unauthorized access",
  "message": "The provided UUID is not authorized"
}
```
Status: 403 Forbidden
