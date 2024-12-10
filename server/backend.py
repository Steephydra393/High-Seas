# This is the all mighty backend server that will handle all the requests from the frontend

from flask import Blueprint, jsonify

backend_blueprint = Blueprint("backend", __name__)

@backend_blueprint.route("/api", methods=["GET"])
def index():
    return jsonify({"message": "Hello from the backend!"})
