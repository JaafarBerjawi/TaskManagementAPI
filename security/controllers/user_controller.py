from flask import request, jsonify, Blueprint
from injector import inject
from security.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'])
@inject
def create_user(user_service: UserService):
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username:
        return jsonify({"error": "Username is required."}), 400
    if not password:
        return jsonify({"error": "Password is required."}), 400

    response, status_code = user_service.create_user(username, password)
    return jsonify(response), status_code
