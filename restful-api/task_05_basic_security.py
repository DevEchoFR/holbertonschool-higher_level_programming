#!/usr/bin/python3
"""
task_05_basic_security.py
Basic HTTP Auth + JWT Auth + Role-based access control (admin-only)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key-change-me"
app.config["JWT_SECRET_KEY"] = "jwt-super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user store (as required)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ----------------------------
# Basic Authentication (HTTP Basic)
# ----------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def basic_auth_error(status):
    # Ensure missing/invalid basic auth is 401
    return jsonify({"error": "Unauthorized"}), 401


@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


# ----------------------------
# JWT Authentication
# ----------------------------
@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not password or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
    )
    return jsonify({"access_token": access_token}), 200


@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


@app.get("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


# ----------------------------
# JWT Error Handlers (MUST be 401 consistently for auth errors)
# ----------------------------
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
