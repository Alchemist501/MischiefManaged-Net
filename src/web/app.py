# File: src/web/app.py

from flask import Flask, jsonify
import sys
import os

# This allows the app to find the 'utils' module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db import get_all_devices
from utils.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

@app.route('/api/devices')
def api_get_devices():
    """API endpoint to get the list of discovered devices."""
    logger.info("API request received for /api/devices")
    devices = get_all_devices()
    return jsonify(devices)