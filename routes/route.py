from flask import request
from flask import Blueprint
from controllers.todoConroller import *
from controllers.userController import *
routes = Blueprint('routes', __name__)

@routes.route('/user', methods=['POST'])
def add_user_route():
    data = request.json
    username = data.get('username')
    return add_user(username)

@routes.route('/todo', methods=['GET'])
def get_todo_list_route():
    username = request.args.get('username')
    return get_todo_list(username)

@routes.route('/todo', methods=['POST'])
def add_todo_task_route():
    data = request.json
    username = data.get('username')
    task = data.get('task')
    return add_todo_task(username, task)

@routes.route('/todo/delete', methods=['DELETE'])
def delete_todo_task_route():
    data = request.json
    task_id = data.get('task_id')
    username = data.get('username')
    return delete_todo_task(task_id, username)

@routes.route('/todo/update', methods=['PUT'])
def update_todo_task_route():
    data = request.json
    task_id = data.get('task_id')
    username = data.get('username')
    task = data.get('task')
    return update_todo_task(task_id, username, task)
