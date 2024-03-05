from flask import jsonify
from models.dbModel import User, Task

def get_todo_list(username):
    try:
        user = User.get(User.username == username)
        todo_list = [{'id': task.id, 'task': task.task_description} for task in user.tasks]
        return jsonify(todo_list)
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

def add_todo_task(username, task):
    try:
        user = User.get(User.username == username)
        Task.create(user=user, task_description=task)
        return jsonify({'message': 'Task added successfully'})
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

def delete_todo_task(task_id, username):
    try:
        user = User.get(User.username == username)
        task = Task.get(Task.id == task_id, Task.user == user)
        task.delete_instance()
        return jsonify({'message': f'Task {task_id} deleted successfully'})
    except (User.DoesNotExist, Task.DoesNotExist):
        return jsonify({'error': 'User or Task not found'}), 404

def update_todo_task(task_id, username, task_text):
    try:
        user = User.get(User.username == username)
        task = Task.get(Task.id == task_id, Task.user == user)
        task.task_description = task_text
        task.save()
        return jsonify({'message': f'Task {task_id} updated successfully'})
    except (User.DoesNotExist, Task.DoesNotExist):
        return jsonify({'error': 'User or Task not found'}), 404