from database import db
from task_management.data_access.task_data_manager_ABC import TaskDataManagerABC
from task_management.entities.task import Task


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)


class TaskDataManager(TaskDataManagerABC):
    @staticmethod
    def to_entity(task_model: TaskModel) -> Task:
        return Task(task_model.id, task_model.user_id, task_model.title, task_model.description, task_model.completed)

    @staticmethod
    def from_entity(task: Task) -> TaskModel:
        return TaskModel(id=task.id, user_id=task.user_id, title=task.title, description=task.description,
                         completed=task.completed)

    def create_task(self, task: Task):
        task_model = TaskDataManager.from_entity(task)
        db.session.add(task_model)
        db.session.commit()
        return task_model.id

    def get_tasks(self, user_id):
        task_models =  TaskModel.query.filter_by(user_id=user_id).all()
        return [TaskDataManager.to_entity(task_model) for task_model in task_models]

    def get_task(self, task_id):
        task_model = TaskModel.query.get(task_id)
        if task_model:
            return TaskDataManager.to_entity(task_model)

    def update_task(self, task: Task):
        task_model = TaskModel.query.get(task.id)
        if task_model:
            task_model.title = task.title
            task_model.description = task.description
            task_model.completed = task.completed
            db.session.commit()
            return True
        return False

    def delete_task(self, task_id):
        task_model = TaskModel.query.get(task_id)
        if task_model:
            db.session.delete(task_model)
            db.session.commit()
            return True
        return False
