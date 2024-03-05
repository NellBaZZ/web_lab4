import requests

# URL вашего приложения Flask, куда будет отправлен запрос на обновление задачи
url = 'http://localhost:5000/todo/update'  # Предполагаем, что id задачи для обновления - 1

# JSON-данные для отправки
data = {'task_id': '4','username': 'stalin', 'task': 'im updated suka'}  # Новое описание задачи

# Отправляем PUT-запрос на обновление задачи пользователя
response = requests.put(url, json=data)

# Выводим результат запроса
print(response.json())
