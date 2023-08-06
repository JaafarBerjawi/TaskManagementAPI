import uuid
from datetime import datetime, timedelta
from flask import jsonify
from injector import inject
from security.entities.user_token import UserToken
from security.data_access.user_token_data_manager_ABC import UserTokenDataManagerABC
from security.services.user_service import UserService


class UserTokenService:
    @inject
    def __init__(self, user_service: UserService, user_token_data_manager: UserTokenDataManagerABC):
        self.user_token_data_manager = user_token_data_manager
        self.user_service = user_service

    def create_user_token(self, username, password):
        is_valid, user_id = self.user_service.validate_user(username, password)
        if not is_valid:
            if user_id:
                return {'message': 'Incorrect Password'}, 401
            else:
                return {'message': 'User not found'}, 404

        # Check if a user token with the given user ID already exists
        existing_user_token = self.user_token_data_manager.get_user_token_by_user_id(user_id)
        token = self.generate_token()
        if existing_user_token:
            # If a token already exists, update it with a new token and expiration date
            token_expiration_date = datetime.now() + timedelta(hours=3)
            existing_user_token.token = token
            existing_user_token.expiration_date = token_expiration_date
            self.user_token_data_manager.update_user_token(existing_user_token)
        else:
            # If no token exists, create a new one
            token_expiration_date = datetime.now() + timedelta(hours=3)
            self.user_token_data_manager.create_user_token(UserToken(user_id, token, token_expiration_date))

        return {"token": token, "expirationDate": token_expiration_date}, 200


    def generate_token(self):
        new_uuid = uuid.uuid4()
        return str(new_uuid)

    def get_active_user_token_by_token(self, token):
        return self.user_token_data_manager.get_active_user_token_by_token(token)
