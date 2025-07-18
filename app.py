# --- Imports ---
import logging
from config import Config
import os
from dotenv import load_dotenv
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from waitress import serve
from extensions import init_extensions,freezer


# --- Environment Setup ---
load_dotenv()

# --- Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# --- Flask App Initialization ---
app = Flask(__name__)
app.config.from_object(Config)

# app.py
app.config['FREEZER_BASE_URL'] = '/ecommarcesite.github.io/'  # e.g., '/my-flask-app/'
app.config['FREEZER_DESTINATION'] = './build'

# Initialize extensions
freezer.init_app(app)  # Initialize Frozen-Flask

# --- Configuration ---
# Secret Key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'a-very-insecure-default-key-change-me')
if app.config['SECRET_KEY'] == 'a-very-insecure-default-key-change-me':
    logger.warning("Using default SECRET_KEY. Set a strong SECRET_KEY environment variable for production.")

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
if not app.config['SQLALCHEMY_DATABASE_URI']:
    raise ValueError("DATABASE_URI environment variable must be set.")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CSRF Protection
app.config['WTF_CSRF_ENABLED'] = True

# Debug Mode
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', '0') == '1'

# --- Initialize Extensions ---
csrf = CSRFProtect(app)
init_extensions(app)
freezer.init_app(app)

# --- Routes ---
from routes import *

# --- Run Application ---
if __name__ == '__main__':
    port = int(os.getenv('PORT',8080))
    host = os.getenv('HOST', '127.0.0.1')  # Allow host to be set via environment variable

    logger.info(f"Application is running in {'DEBUG' if app.config['DEBUG'] else 'PRODUCTION'} mode.")
    
    if app.config['DEBUG']:
        logger.info(f"Starting development server on http://{host}:{port}")
        app.run(host=host, port=port, debug=True)
    else:
        logger.info(f"Starting Waitress server on {host}:{port}")
        serve(app, host=host, port=port)
