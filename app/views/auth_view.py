from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import register_user, login_user

auth_blueprint = Blueprint('auth',__name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user=register_user(data)
    return jsonify({'id': user.id, 'email': user.email}), 201

@auth_blueprint.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    token = login_user(data)
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

