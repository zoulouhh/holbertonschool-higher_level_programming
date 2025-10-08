#!/usr/bin/python3
"""
A simple RESTful API built with Flask.
Demonstrates handling routes, serving JSON, and managing POST requests.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_data():
    """Return list of usernames in the users dictionary."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return data for a specific user."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user via POST request.
    Expected JSON:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    """
    data = request.get_json()

    # Validate incoming JSON
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data  # Store the entire user data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    # Run Flask development server
    app.run(host="0.0.0.0", port=5000)
