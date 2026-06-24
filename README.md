# Todo-list

        #HOW TO LAUNCH LOCALLY

ENDPOINTS:
1. Получить список всех задач
URL: /api/v1/tasks

Метод: GET

Параметры фильтрации (Query params):

is_completed (bool, необязательный): true (только выполненные) или false (только активные).

Пример успешного ответа (200 OK):

JSON
[
  {
    "id": 1,
    "created_at": "24.06.26 18:55:00",
    "status": "Not Completed",
    "title": "Купить молоко",
    "description": "3.2% жирности"
  }
]
2. Получить конкретную задачу по ID
URL: /api/v1/tasks/{task_id}

Метод: GET

Пример успешного ответа (200 OK):

JSON
{
  "id": 1,
  "created_at": "24.06.26 18:55:00",
  "status": false,
  "title": "Купить молоко",
  "description": "3.2% жирности"
}
3. Создать новую задачу
URL: /api/v1/tasks

Метод: POST

Пример тела запроса (JSON Request):

JSON
{
  "title": "Выучить FastAPI",
  "description": "Разобраться со слоем репозитория"
}
Пример успешного ответа (200 OK):

JSON
{
  "message": "Task created successfully",
  "task": {
    "id": 2,
    "created_at": "24.06.26 19:10:15",
    "status": false,
    "title": "Выучить FastAPI",
    "description": "Разобраться со слоем репозитория"
  }
}
4. Отметить задачу как выполненную
URL: /api/v1/tasks/{task_id}

Метод: PUT

Пример успешного ответа (200 OK):

JSON
{
  "message": "Task completed successfully",
  "task": {
    "id": 2,
    "created_at": "24.06.26 19:10:15",
    "status": true,
    "title": "Выучить FastAPI",
    "description": "Разобраться со слоем репозитория"
  }
}
5. Удалить задачу
URL: /api/v1/tasks/{task_id}

Метод: DELETE

Пример успешного ответа (200 OK):

JSON
{
  "message": "Task deleted successfully"
}

ERROR CODES:
400 - bad request
404 - data not found
409 - status conflict
422 - unavailable option
500 - internal server error
