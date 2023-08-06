from security.data_access.user_data_manager_ABC import UserDataManagerABC
from security.entities.user import User


class UserDataManager(UserDataManagerABC):
    def __init__(self):
        user1 = User('Jaafar', '1', 1)
        user2 = User('Jaafar2', '2', 2)
        self.users = [user1, user2]

    def create_user(self, user: User):
        user.id = len(self.users)
        self.users.append(user)

    def validate_user(self, username, password):
        user = self.get_user_by_username(username)
        if not user:
            return False, None
        if user.password != password:
            return False, user.id
        return True, user.id

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
