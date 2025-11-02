from flask import Blueprint, request, jsonify
from app.controllers.user_controller import get_all_users, create_user, get_user_by_id
from app.utils.errors import NotFoundError
from app.utils.response import success_response
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    all_users = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]
    return success_response(all_users)

# @user_blueprint.route('/users', methods=['POST'])
# def add_user():
#     data = request.get_json()
#     user = create_user(data)
#     return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

# single user data
@user_blueprint.route("/users/<int:user_id>", methods=['GET'])
def single_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise NotFoundError("User not found")

    return success_response(user.to_dict())



