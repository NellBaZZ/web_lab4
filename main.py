from flask import Flask, jsonify, request

app = Flask(__name__)

# Храним тут пользователей и их задачи
users = {}

# Добавление пользователя
@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if username not in users:
        users[username] = []
        return jsonify({'message': f'User {username} added successfully'})
    else:
        return jsonify({'error': 'User already exists'}), 400

# Просмотр списка задач
@app.route('/todo', methods=['GET'])
def get_todo():
    username = request.args.get('username')
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    todo_list = [{'id': idx, 'task': task} for idx, task in enumerate(users[username])]
    return jsonify(todo_list)

# Добавление задачи пользователя
@app.route('/todo', methods=['POST'])
def add_todo():
    data = request.json
    username = data.get('username')
    task = data.get('task')
    if username in users:
        users[username].append(task)
        return jsonify({'message': 'Task added successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

# Удаление задачи пользователя
@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    username = request.args.get('username')
    if username in users:
        if id < len(users[username]):
            del users[username][id]
            return jsonify({'message': f'Task {id} deleted successfully'})
        else:
            return jsonify({'error': 'Task not found'}), 404
    else:
        return jsonify({'error': 'User not found'}), 404

# Обновление задачи пользователя
@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    username = data.get('username')
    task = data.get('task')
    if username in users:
        if id < len(users[username]):
            users[username][id] = task
            return jsonify({'message': f'Task {id} updated successfully'})
        else:
            return jsonify({'error': 'Task not found'}), 404
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

