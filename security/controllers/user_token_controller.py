from flask import request, jsonify, Blueprint
from injector import inject
from security.services.user_token_service import UserTokenService

user_token_bp = Blueprint('user_token_bp', __name__)


@user_token_bp.route('/authenticate', methods=['POST'])
@inject
def create_user(user_token_service: UserTokenService):
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username:
        return jsonify({"error": "Username is required."}), 400
    if not password:
        return jsonify({"error": "Password is required."}), 400

    response, status_code = user_token_service.create_user_token(username, password)
    return jsonify(response), status_code
