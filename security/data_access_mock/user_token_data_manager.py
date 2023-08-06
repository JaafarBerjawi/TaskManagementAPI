from _datetime import datetime, timedelta
from security.data_access.user_token_data_manager_ABC import UserTokenDataManagerABC
from security.entities.user_token import UserToken


class UserTokenDataManager(UserTokenDataManagerABC):
    def __init__(self):
        current_date = datetime.now()
        user_token_1 = UserToken(1, 'Token1', current_date + timedelta(hours=3), 1)
        user_token_2 = UserToken(2, 'Token2', current_date + timedelta(hours=-1), 2)
        self.user_tokens = [user_token_1, user_token_2]

    def create_user_token(self, user_token: UserToken):
        user_token.id = len(self.user_tokens)
        self.user_tokens.append(user_token)

    def get_active_user_token_by_token(self, token):
        for user_token in self.user_tokens:
            if user_token.token == token and user_token.expiration_date > datetime.now():
                return user_token
        return None

    def update_user_token(self, user_token: UserToken):
        # Find the user token with the given user_id in the list of user tokens and update it.
        for i, existing_token in enumerate(self.user_tokens):
            if existing_token.user_id == user_token.user_id:
                self.user_tokens[i] = user_token
                break

    def get_user_token_by_user_id(self, user_id):
        # Find the user token with the given user_id in the list of user tokens.
        for user_token in self.user_tokens:
            if user_token.user_id == user_id:
                return user_token
        return None
