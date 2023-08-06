from injector import Module, Binder
from security.data_access.user_data_manager_ABC import UserDataManagerABC
from security.data_access.user_token_data_manager_ABC import UserTokenDataManagerABC
from security.services.user_service import UserService
from security.services.user_token_service import UserTokenService
from task_management.data_access.task_data_manager_ABC import TaskDataManagerABC
from task_management.entities.task import Task
from task_management.services.task_service import TaskService
from security.services.encyption.encryption_service_ABC import EncryptionServiceABC
import unittest
from injector import Injector


class ServiceModule(Module):
    def configure(self, binder: Binder):
        from security.data_access_mock.user_data_manager import UserDataManager as UserDataManager
        from security.data_access_mock.user_token_data_manager import UserTokenDataManager as UserTokenDataManager
        binder.bind(UserDataManagerABC, to=UserDataManager)
        binder.bind(UserService, to=UserService)
        binder.bind(UserTokenDataManagerABC, to=UserTokenDataManager)
        binder.bind(UserTokenService, to=UserTokenService)
        binder.bind(TaskService, to=TaskService)
        from task_management.data_access_mock.task_data_manager import TaskDataManager
        binder.bind(TaskDataManagerABC, to=TaskDataManager)
        from security.services.encyption.encryption_service_mock import EncryptionServiceMock
        binder.bind(EncryptionServiceABC, to=EncryptionServiceMock)


class AppTestCase(unittest.TestCase):
    def setUp(self):
        injector = Injector([ServiceModule()])
        self.user_service = injector.get(UserService)
        self.user_token_service = injector.get(UserTokenService)
        self.task_service = injector.get(TaskService)

    def tearDown(self):
        pass

    def test_create_user_with_success(self):
        response, status_code = self.user_service.create_user("testuser", "testpassword")
        self.assertEqual(status_code, 200)

    def test_create_user_fail_username_already_exists(self):
        response, status_code = self.user_service.create_user("Jaafar", "testpassword")
        self.assertEqual(status_code, 400)

    def test_authenticate_success(self):
        response, status_code = self.user_token_service.create_user_token("Jaafar", "1")
        self.assertEqual(status_code, 200)

    def test_authenticate_fail_user_not_found(self):
        response, status_code = self.user_token_service.create_user_token("Jaafar5", "1")
        self.assertEqual(status_code, 404)

    def test_authenticate_fail_wrong_password(self):
        response, status_code = self.user_token_service.create_user_token("Jaafar", "10")
        self.assertEqual(status_code, 401)

    def test_create_task_success(self):
        task = Task(None, 1, "TestTask", "TestTask Desc", False)
        response, status_code = self.task_service.create_task(task)
        self.assertEqual(status_code, 200)

    def test_get_tasks_success(self):
        user_id = 2
        response, status_code = self.task_service.get_tasks(user_id)
        self.assertEqual(status_code, 200)
        self.assertEqual(len(response), 1)

    def test_get_task_success(self):
        task_id = 3
        response, status_code = self.task_service.get_task(task_id, 2)
        self.assertEqual(status_code, 200)

    def test_get_task_fail_task_not_found(self):
        task_id = 1000
        response, status_code = self.task_service.get_task(task_id, 2)
        self.assertEqual(status_code, 404)

    def test_get_task_fail_unauthorized(self):
        task_id = 3
        response, status_code = self.task_service.get_task(task_id, 1)
        self.assertEqual(status_code, 403)

    def test_update_task_success(self):
        task_to_update = Task(3, 2, "UpdateTitle", "UpdatedDescription", False)
        response, status_code = self.task_service.update_task(task_to_update)
        self.assertEqual(status_code, 200)

    def test_update_task_fail_task_not_found(self):
        task_to_update = Task(100, 2, "UpdateTitle", "UpdatedDescription", False)
        response, status_code = self.task_service.update_task(task_to_update)
        self.assertEqual(status_code, 404)

    def test_update_task_fail_unauthorized(self):
        task_to_update = Task(3, 100, "UpdateTitle", "UpdatedDescription", False)
        response, status_code = self.task_service.update_task(task_to_update)
        self.assertEqual(status_code, 403)

    def test_delete_task_success(self):
        response, status_code = self.task_service.delete_task(2, 1)
        self.assertEqual(status_code, 200)
        get_tasks_response, get_tasks_status_code = self.task_service.get_tasks(1)
        self.assertEqual(len(get_tasks_response), 1)

    def test_delete_task_fail_task_not_found(self):
        response, status_code = self.task_service.delete_task(100, 1)
        self.assertEqual(status_code, 404)

    def test_delete_task_fail_unauthorized(self):
        response, status_code = self.task_service.delete_task(1, 100)
        self.assertEqual(status_code, 403)
