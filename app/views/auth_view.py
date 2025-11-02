from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import register_user, login_user
from app.utils.errors import AppError
from app.utils.response import success_response

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        raise AppError("Missing JSON body", 400)

    user = register_user(data)  # may raise AppError internally
    return success_response({'id': user.id, 'email': user.email},"User registration successful",201)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        raise AppError("Missing JSON body", 400)

    token = login_user(data)
    if token:
        return success_response({'token': token},"User logged in successfully",201)

    raise AppError("Invalid credentials", 401)
