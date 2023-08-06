from _datetime import datetime
from database import db
from security.data_access.user_token_data_manager_ABC import UserTokenDataManagerABC
from security.entities.user_token import UserToken


class UserTokenModel(db.Model):
    __tablename__ = 'user_tokens'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    token = db.Column(db.String(100), nullable=False, index=True)
    expiration_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, token, expiration_date):
        self.user_id = user_id
        self.token = token
        self.expiration_date = expiration_date


class UserTokenDataManager(UserTokenDataManagerABC):
    def __init__(self):
        pass

    @staticmethod
    def to_entity(user_token_model: UserTokenModel) -> UserToken:
        if not user_token_model:
            return None
        return UserToken(user_token_model.user_id, user_token_model.token, user_token_model.expiration_date,
                         user_token_model.id)

    @staticmethod
    def from_entity(user_token: UserToken) -> UserTokenModel:
        return UserTokenModel(user_token.user_id, user_token.token, user_token.expiration_date)

    def create_user_token(self, user_token: UserToken):
        user_token_model = UserTokenDataManager.from_entity(user_token)
        db.session.add(user_token_model)
        db.session.commit()

    def get_active_user_token_by_token(self, token):
        current_datetime = datetime.now()
        user_token = (db.session.query(UserTokenModel).filter_by(token=token)
                      .filter(UserTokenModel.expiration_date > current_datetime).first())
        return UserTokenDataManager.to_entity(user_token)

    def update_user_token(self, user_token: UserToken):
        # Get the existing user token by ID
        existing_user_token = UserTokenModel.query.get(user_token.id)

        if existing_user_token is None:
            raise Exception("User token not found")

        # Update the fields of the existing user token with the new values
        existing_user_token.token = user_token.token
        existing_user_token.expiration_date = user_token.expiration_date

        # Commit the changes to the database
        db.session.commit()

    def get_user_token_by_user_id(self, user_id):
        # Retrieve the user token from the database based on the provided user_id
        user_token = UserTokenModel.query.filter_by(user_id=user_id).first()

        # If the user token is not found, return None
        if user_token is None:
            return None

        # Otherwise, return the user token entity
        return UserTokenDataManager.to_entity(user_token)
