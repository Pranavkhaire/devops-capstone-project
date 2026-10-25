
"""
Package: service
Package for the application models and service routes.
This module creates and configures the Flask app and sets up logging
and the SQL database.
"""

import sys

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from service import config
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# Configure security headers using Flask-Talisman.
# Disable HTTPS redirection for the local lab and test environment.
talisman = Talisman(
    app,
    force_https=False,
    content_security_policy=None,
)

# Enable Cross-Origin Resource Sharing (CORS) for API access.
cors = CORS(app)

# Import routes after the Flask app is created.
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402

# pylint: disable=wrong-import-position
from service.common import error_handlers, cli_commands  # noqa: F401 E402

# Set up logging for production.
log_handlers.init_logging(app, "gunicorn.error")

# Initialize the database.
try:
    models.init_db(app)
except Exception as error:
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)
