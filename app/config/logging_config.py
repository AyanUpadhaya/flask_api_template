import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../logs")
    os.makedirs(log_dir, exist_ok=True)

    # Define log file paths
    info_log = os.path.join(log_dir, "info.log")
    error_log = os.path.join(log_dir, "error.log")

    # Clear default Flask handlers (optional)
    for handler in app.logger.handlers[:]:
        app.logger.removeHandler(handler)

    # --- Info & Debug Logs ---
    info_handler = RotatingFileHandler(info_log, maxBytes=5*1024*1024, backupCount=3)
    info_handler.setLevel(logging.INFO)
    info_formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
    )
    info_handler.setFormatter(info_formatter)

    # --- Error Logs ---
    error_handler = RotatingFileHandler(error_log, maxBytes=5*1024*1024, backupCount=3)
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s - [in %(pathname)s:%(lineno)d]"
    )
    error_handler.setFormatter(error_formatter)

    # Add both handlers
    app.logger.addHandler(info_handler)
    app.logger.addHandler(error_handler)
    app.logger.setLevel(logging.INFO)

    # app.logger.info("Logging setup complete.")

"""
use logging anywhere

from flask import Blueprint
from app.utils.errors import AppError
import logging

user_blueprint = Blueprint("user", __name__)
logger = logging.getLogger(__name__)

@user_blueprint.route("/users/<int:user_id>")
def get_user(user_id):
    logger.info(f"Fetching user with id: {user_id}")

    if user_id != 1:
        logger.error(f"User with id {user_id} not found")
        raise AppError("User not found", 404)
"""