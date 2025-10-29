# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    CORS(app)

    from app.views.main_view import main_blueprint
    from app.views.user_view import user_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/api/v1')

    # 🔧 Custom 404 handler
    from flask import request, jsonify, render_template

    @app.errorhandler(404)
    def not_found(error):
        # Return JSON for API routes
        if request.path.startswith('/api') or request.path.startswith('/users'):
            return jsonify({"error": "API endpoint not found"}), 404
        # Return HTML for regular pages
        return render_template("404.html"), 404

    return app
