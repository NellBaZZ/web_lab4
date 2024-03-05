from flask import jsonify
from models.dbModel import User

def add_user(username):
    try:
        user = User.create(username=username)
        return jsonify({'message': f'User {username} added successfully'})
    except:
        return jsonify({'error': 'User already exists'}), 400