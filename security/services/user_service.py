from flask import jsonify
from injector import inject
from security.entities.user import User
from security.data_access.user_data_manager_ABC import UserDataManagerABC
from security.services.encyption.encryption_service_ABC import EncryptionServiceABC


class UserService:
    @inject
    def __init__(self, user_data_manager: UserDataManagerABC, encryption_service: EncryptionServiceABC):
        self.user_data_manager = user_data_manager
        self.encryption_service = encryption_service

    def create_user(self, username, password):
        existing_user = self.user_data_manager.get_user_by_username(username)
        if existing_user:
            return {'error': 'User already exists'}, 400

        hashed_password = self.encryption_service.encrypt(password)

        # Create the user and store it in the database
        user = User(username, hashed_password)
        self.user_data_manager.create_user(user)

        return {}, 200

    def validate_user(self, username, password):
        hashed_password = self.encryption_service.encrypt(password)
        return self.user_data_manager.validate_user(username, hashed_password)
