
"""
Package: service
Package for the application models and service routes.
This module creates and configures the Flask app and sets up logging
and the SQL database.

"""

from flask_cors import CORS
import sys
from flask import Flask
from flask_talisman import Talisman

from service import config
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# Add security headers.
# Disable HTTPS redirection for the local lab and test environment.
Talisman(
    app,
    force_https=False,
    content_security_policy=None,
)
# Enable CORS for API access
CORS(app)
# Import routes after the Flask app is created
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402

# pylint: disable=wrong-import-position
from service.common import error_handlers, cli_commands  # noqa: F401 E402

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   SERVICE   RUNNING  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.init_db(app)
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

app.logger.info("Service initialized!")
