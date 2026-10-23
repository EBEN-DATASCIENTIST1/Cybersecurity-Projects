
from collections import defaultdict
from time import time

from flask import Flask, jsonify, request

app = Flask(__name__)

# Fictional account for local security testing only.
TEST_USERNAME = "lab_user"
TEST_PASSWORD = "LabPass123!"

MAX_ATTEMPTS = 5
BLOCK_SECONDS = 30

failed_attempts = defaultdict(list)
blocked_until = {}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Local password security lab",
        "login_endpoint": "/login",
        "scope": "Local testing only"
    })


@app.route("/login", methods=["POST"])
def login():
    # Allow requests only from the local machine.
    if request.remote_addr not in ("127.0.0.1", "::1"):
        return jsonify({"message": "Local access only"}), 403

    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify({"message": "Invalid request"}), 400

    client_ip = request.remote_addr
    now = time()

    # Remove failed attempts older than the block window.
    failed_attempts[client_ip] = [
        attempt for attempt in failed_attempts[client_ip]
        if now - attempt < BLOCK_SECONDS
    ]

    # Check whether the client is temporarily blocked.
    if now < blocked_until.get(client_ip, 0):
        return jsonify({
            "message": "Too many failed attempts. Try again later."
        }), 429

    # Check the fictional lab credentials.
    if username == TEST_USERNAME and password == TEST_PASSWORD:
        failed_attempts[client_ip].clear()
        blocked_until.pop(client_ip, None)
        return jsonify({"message": "Welcome to the lab!"}), 200

    failed_attempts[client_ip].append(now)

    # Temporarily block after too many failed attempts.
    if len(failed_attempts[client_ip]) >= MAX_ATTEMPTS:
        blocked_until[client_ip] = now + BLOCK_SECONDS
        return jsonify({
            "message": "Too many failed attempts. Try again later."
        }), 429

    return jsonify({"message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
