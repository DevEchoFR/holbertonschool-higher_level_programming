#!/usr/bin/python3
"""
task_04_flask.py
A simple Flask REST API storing users in-memory.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory: {username: user_object}
# NOTE: Do not include testing data here.
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return a list of all usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse JSON safely and detect invalid JSON bodies
    try:
        payload = request.get_json(silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if payload is None or not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the whole object as the value (as required)
    users[username] = payload

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
