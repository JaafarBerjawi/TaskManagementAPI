from database import db
from security.data_access.user_data_manager_ABC import UserDataManagerABC
from security.entities.user import User


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserDataManager(UserDataManagerABC):
    def __init__(self):
        pass

    @staticmethod
    def to_entity(user_model: UserModel) -> User:
        return User(user_model.username, user_model.password)

    @staticmethod
    def from_entity(user: User) -> UserModel:
        return UserModel(username=user.username, password=user.password)

    def create_user(self, user: User):
        user_model = UserDataManager.from_entity(user)
        db.session.add(user_model)
        db.session.commit()

    def validate_user(self, username, password):
        user = db.session.query(UserModel).filter_by(username=username).first()
        if not user:
            return False, None
        if user.password != password:
            return False, user.id
        return True, user.id

    def get_user_by_username(self, username):
        user_model = db.session.query(UserModel).filter_by(username=username).first()
        if user_model:
            return UserDataManager.to_entity(user_model)
