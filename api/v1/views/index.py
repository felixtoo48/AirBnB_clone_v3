#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

# Create a route /status on the app_views object
# that returns a JSON: {"status": "OK"}
@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})
