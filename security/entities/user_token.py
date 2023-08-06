class UserToken:
    def __init__(self, user_id, token, expiration_date, id=None):
        self.id = id
        self.user_id = user_id
        self.token = token
        self.expiration_date = expiration_date
