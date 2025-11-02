# app/__init__.py
import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from dotenv import load_dotenv
from flask_migrate import Migrate
from app.config.logging_config import setup_logging
load_dotenv()  # Load variables from .env

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    CORS(app)
    from app.middlewares.error_handlers import register_error_handlers
    from app.views.main_view import main_blueprint
    from app.views.user_view import user_blueprint
    from app.views.auth_view import auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/api/v1')
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1')

    # logging setup
    setup_logging(app)

    # 🔧 Custom 404 handler
    @app.errorhandler(404)
    def not_found(error):
        # Return JSON for API routes
        if request.path.startswith('/api'):
            return jsonify({"error": "API endpoint not found"}), 404
        # Return HTML for regular pages
        return render_template("404.html"), 404

    # global error handler
    register_error_handlers(app)

    return app

""" FOR DB MIGRATION
flask db init
flask db migrate -m "Add password and created_at to User"
flask db upgrade
"""