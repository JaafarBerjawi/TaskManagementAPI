from abc import ABC, abstractmethod
from security.entities.user_token import UserToken


class UserTokenDataManagerABC(ABC):
    @abstractmethod
    def create_user_token(self, user_token: UserToken):
        pass

    @abstractmethod
    def get_active_user_token_by_token(self, token):
        pass

    @abstractmethod
    def update_user_token(self, user_token: UserToken):
        pass

    @abstractmethod
    def get_user_token_by_user_id(self, user_id):
        pass
