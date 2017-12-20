#!/usr/bin/python3
"""API"""

import os
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, Response

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close(self):
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='Not found'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)