from flask import Blueprint, request, jsonify
from app.controllers.user_controller import get_all_users, create_user

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

@user_blueprint.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201




