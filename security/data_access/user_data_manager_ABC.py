from abc import ABC, abstractmethod
from security.entities.user import User


class UserDataManagerABC(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def validate_user(self, username, password):
        pass

    @abstractmethod
    def get_user_by_username(self, username):
        pass
