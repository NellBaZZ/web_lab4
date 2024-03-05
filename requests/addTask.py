import requests

# URL вашего приложения Flask, куда будет отправлен запрос на добавление задачи
url = 'http://localhost:5000/todo'

# JSON-данные для отправки
data = {'username': 'stalin', 'task': 'Example task'}

# Отправляем POST-запрос на добавление задачи для пользователя
response = requests.post(url, json=data)

# Выводим результат запроса
print(response.json())
