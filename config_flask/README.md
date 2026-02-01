# Flask Configuration API

This directory contains the Flask-based REST API for managing the athena configuration.

## Overview

The Flask Configuration API provides a web-based interface for managing various configuration settings for cluster control systems. It's built on top of the existing `config_lib` modules but exposes them via HTTP endpoints.

## Configuration Types

The following configuration types are supported:

- **android** - Android-specific configurations
- **athena** - Athena client and daemon configurations
- **client** - Client configuration and ID management
- **combiner** - Combiner configuration
- **emulators** - Emulator configurations
- **local** - Local configuration settings
- **manual** - Manual configuration overrides
- **overrides** - Configuration overrides
- **remote** - Remote host configurations
- **steam** - Steam client and game configurations
- **web** - Web browser configurations
- **windows_games** - Windows games configuration

## Running the API

1. Install dependencies:
```bash
pip install flask
```

2. Run the API server:
```bash
cd config_flask
python -m flask run --host=0.0.0.0 --port=5000 --debug=True
```

The API will be available at `http://localhost:5000`

## API Endpoints

### General Endpoints

- `GET /` - API health check and information
- `GET /api/<config_type>/<operation>` - Fetch configuration
- `POST /api/<config_type>/<operation>` - Update configuration

### Endpoint Format

All endpoints follow this pattern:
```
/api/{config_type}/{operation}
```

- `config_type`: One of the supported configuration types above
- `operation`: The specific operation to perform

## Usage Examples

### Fetch Configuration

Example: Fetch Android configuration
```bash
curl http://localhost:5000/api/android/fetch_config
```

Example: Fetch client ID
```bash
curl http://localhost:5000/api/client/fetch_id
```

### Update Configuration

Example: Update client ID
```bash
curl -X POST http://localhost:5000/api/client/update_id \
  -H "Content-Type: application/json" \
  -d '{"id": "client123"}'
```

### Endpoint Parameters

If you want to not update the client configuration file you can pass in `is_client` as false. Default value is true.

```bash
# Set is_client parameter
curl "http://localhost:5000/api/config/remote/fetch_hosts?is_client=false"
```

## Response Format

### Success Responses

All successful responses return JSON with the following structure:

```json
{
  "status": "success",
  "data": { ... }
}
```

### Error Responses

Error responses follow this structure:

```json
{
  "error": "Error message details"
}
```
