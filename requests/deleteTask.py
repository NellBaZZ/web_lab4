import requests

# URL вашего приложения Flask, куда будет отправлен запрос на удаление задачи
url = 'http://localhost:5000/todo/delete'  # Замените '1' на фактический индекс задачи, которую нужно удалить

data = {'task_id': '4','username': 'stalin', 'task': 'im updated suka'}
# Отправляем DELETE-запрос на удаление задачи
response = requests.delete(url, json=data)

# Выводим результат запроса
print(response.json())
