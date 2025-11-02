from flask import Flask, jsonify, request
from app.utils.errors import AppError
import logging
logger = logging.getLogger(__name__)

def register_error_handlers(app: Flask):

    @app.errorhandler(AppError)
    def handle_app_error(error):
        app.logger.error(
            f"{error.__class__.__name__}: {error.message} "
            f"[Status: {error.status_code}, Path: {request.path}]"
        )
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception("Unhandled Exception: %s", error)
        response = jsonify({
            "status": "error",
            "message": "Something went wrong on the server",
        })
        response.status_code = 500
        return response
