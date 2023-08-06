from abc import ABC, abstractmethod
from task_management.entities.task import Task


class TaskDataManagerABC(ABC):
    @abstractmethod
    def create_task(self, task: Task):
        pass

    @abstractmethod
    def get_tasks(self, user_id):
        pass

    @abstractmethod
    def get_task(self, task_id):
        pass

    @abstractmethod
    def update_task(self, task: Task):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass
