import requests

# URL вашего приложения Flask, куда будет отправлен запрос
url = 'http://localhost:5000/todo'

# Параметры запроса (имя пользователя)
params = {'username': 'stalin'}

# Отправляем GET-запрос на получение списка задач для указанного пользователя
response = requests.get(url, params=params)

# Выводим результат запроса
print(response.json())

