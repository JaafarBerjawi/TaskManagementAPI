from task_management.data_access.task_data_manager_ABC import TaskDataManagerABC
from task_management.entities.task import Task


class TaskDataManager(TaskDataManagerABC):
    def __init__(self):
        # Mock tasks for user 1
        task1_user1 = Task(1, 1, 'Task1 User1', 'Description for Task1 User1', False)
        task2_user1 = Task(2, 1, 'Task2 User1', 'Description for Task2 User1', True)

        # Mock task for user 2
        task1_user2 = Task(3, 2,'Task1 User2', 'Description for Task1 User2', False)

        self.tasks = [task1_user1, task2_user1, task1_user2]

    def create_task(self, task: Task):
        # In the actual implementation, add the task to the list of tasks.
        task.id = len(self.tasks)
        self.tasks.append(task)

    def get_tasks(self, user_id):
        # Return all tasks that belong to the given user_id.
        return [task for task in self.tasks if task.user_id == user_id]

    def get_task(self, task_id):
        # Find the task with the given task_id in the list of tasks.
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task: Task):
        # Find the task with the given task_id in the list of tasks and update it.
        for i, existing_task in enumerate(self.tasks):
            if existing_task.id == task.id:
                self.tasks[i] = task
                return True

    def delete_task(self, task_id):
        # Remove the task with the given task_id from the list of tasks.
        self.tasks = [task for task in self.tasks if task.id != task_id]
