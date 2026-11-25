
from functools import wraps
from flask import request, jsonify
import os


def require_api_key(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        api_key = os.getenv("API_KEY")
        request_key = request.headers.get("X-API-Key")

        if not api_key or request_key != api_key:
            return jsonify({
                "error": "Unauthorized",
                "message": "Invalid or missing API key"
            }), 401

        return function(*args, **kwargs)

    return decorated
