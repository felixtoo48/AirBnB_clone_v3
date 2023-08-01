#!/usr/bin/python3
"""flask"""

from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv

# Create a Flask instance
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views, url_prefix="/api/v1")


# Define a method to handle app teardown
@app.teardown_appcontext
def teardown_appcontext(self):
    """ teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """404ed"""
    return jsonify({"error": "Not found"}), 404


# Run the Flask server
if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
