import requests

# URL вашего приложения Flask, куда будет отправлен запрос
url = 'http://localhost:5000/user'

# JSON-данные для отправки
data = {'username': 'stalin'}

# Отправляем POST-запрос на добавление пользователя
response = requests.post(url, json=data)

# Выводим результат запроса
print(response.json())
