from flask import Blueprint, request, jsonify, abort, g
from task_management.entities.task import Task
from task_management.services.task_service import TaskService
from flask_injector import inject
from security.middlewares.authentication_middleware import needs_authentication

# Create a blueprint for the task API
task_bp = Blueprint('task', __name__)


@task_bp.route('/tasks', methods=['POST'])
@inject
@needs_authentication
def create_task(task_service: TaskService):
    data = request.json
    user_id = g.user_id
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')

    if not title:
        return jsonify({'error': 'Title is required.'}), 400

    task = Task(user_id=user_id, title=title, description=description, completed=completed)
    response, status_code = task_service.create_task(task)
    return jsonify(response), status_code


@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
@inject
@needs_authentication
def get_task(task_id, task_service: TaskService):
    user_id = g.user_id
    response, status_code = task_service.get_task(task_id, user_id)
    return jsonify(response), status_code


@task_bp.route('/tasks', methods=['GET'])
@inject
@needs_authentication
def get_tasks(task_service: TaskService):
    user_id = g.user_id
    response, status_code = task_service.get_tasks(user_id)
    return jsonify(response), status_code


@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@inject
@needs_authentication
def update_task(task_id, task_service: TaskService):
    data = request.json
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')
    user_id = g.user_id

    if not title:
        return jsonify({'error': 'Title is required.'}), 400

    task = Task(id=task_id, user_id=user_id, title=title, description=description, completed=completed)
    response, status_code = task_service.update_task(task)
    return jsonify(response), status_code


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@inject
@needs_authentication
def delete_task(task_id, task_service: TaskService):
    user_id = g.user_id
    response, status_code = task_service.delete_task(task_id, user_id)
    return jsonify(response), status_code
