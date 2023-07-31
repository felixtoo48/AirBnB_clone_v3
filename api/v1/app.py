#!/usr/bin/python3

from flask import Flask
from api.v1.views import app_views
from models import storage

# Create a Flask instance
app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.reguster_blueprint(app_views)

# Define a method to handle app teardown
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


# Run the Flask server
if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
