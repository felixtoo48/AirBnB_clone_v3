#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage


# Create a route /status on the app_views object
# that returns a JSON: {"status": "OK"}
@app_views.route("/status", methods=["GET"])
def get_status():
    """ route/status on app views returning a JSON"""
    return jsonify({"status": "OK"})


@app_views.route("stats", methods=["GET"])
def get_stats():
    """ retrieves the number of each object by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
        }
    return jsonify(stats)
