class Task:
    def __init__(self, id=None, user_id=None, title=None, description=None, completed=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }
