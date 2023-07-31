#!/usr/bin/python3

from flask import Flask, render_template, jsonify
from api.v1.views import app_views
from models import storage
import os

# Create a Flask instance
app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

# Define a method to handle app teardown
@app.teardown_appcontext
def teardown_appcontext(exception):
    """ teardown"""
    storage.close()


# Run the Flask server
if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
