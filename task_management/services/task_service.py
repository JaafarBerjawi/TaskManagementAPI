from flask import jsonify
from injector import inject
from task_management.entities.task import Task
from task_management.data_access.task_data_manager_ABC import TaskDataManagerABC


class TaskService:
    @inject
    def __init__(self, task_data_manager: TaskDataManagerABC):
        self.task_data_manager = task_data_manager

    def create_task(self, task: Task):
        task_id = self.task_data_manager.create_task(task)
        return {'id': task_id}, 200

    def get_tasks(self, user_id):
        tasks = self.task_data_manager.get_tasks(user_id)
        task_dicts = [task.to_dict() for task in tasks]
        return task_dicts, 200

    def get_task(self, task_id, user_id):
        task = self.task_data_manager.get_task(task_id)
        if not task:
            return {'error': 'Task not found'}, 404
        if task.user_id != user_id:
            return {'message': 'You are not authorized to view this task'}, 403
        return task.to_dict(), 200

    def update_task(self, task_to_update: Task):
        task = self.task_data_manager.get_task(task_to_update.id)
        if not task:
            return {'error': 'Task not found'}, 404
        if task.user_id != task_to_update.user_id:
            return {'message': 'You are not authorized to update this task'}, 403
        is_updated = self.task_data_manager.update_task(task_to_update)
        if is_updated:
            return {'message': 'Task updated successfully'}, 200
        return {'error': 'Task not found'}, 404

    def delete_task(self, task_id, user_id):
        task = self.task_data_manager.get_task(task_id)
        if not task:
            return {'error': 'Task not found'}, 404
        if task.user_id != user_id:
            return {'message': 'You are not authorized to delete this task'}, 403
        self.task_data_manager.delete_task(task_id)
        return {'message': 'Task deleted successfully'}, 200
