from datetime import datetime

class Task:
    def __init__(self, title:str = None, description:str = None) -> None:
        self.title = title
        self.description = description
        self.now = datetime.now()
        self.created_at = self.now.strftime("%d.%m.%y %H:%M:%S")
        self.status = "Not completed"


class TaskManager:
    def __init__(self) -> None:
        self.tasks = dict()
        self.counter = 0

    def add_task(self, title: str, description = None) -> None:
        task = Task(title, description)
        self.tasks[self.counter] = task
        self.counter += 1

    def list_tasks(self) -> dict:
        output = self.tasks.copy()
        return output

    def complete_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            raise TaskNotFoundError
        self.tasks[task_id].status = "Completed"

    def delete_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            raise TaskNotFoundError
        self.tasks.pop(task_id)


class TaskNotFoundError(Exception):
    pass