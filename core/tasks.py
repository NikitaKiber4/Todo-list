from datetime import datetime

class Task:
    def __init__(self):
        self.tasks = dict()
        self.counter = 0

    def add_task(self, title: str, description = None) -> None:
        now = datetime.now()
        cur_time = now.strftime("%d.%m.%y %H:%M:%S")
        self.tasks[self.counter] = ((cur_time, title, description) if description else (cur_time, title))
        self.counter += 1

    def list_tasks(self) -> str | list:
        output = []
        for key in self.tasks:
            if len(self.tasks[key]) == 3:
                output.append((key, self.tasks[key][0], self.tasks[key][1], self.tasks[key][2]))
            else:
                output.append((key, self.tasks[key][0], self.tasks[key][1]))
        if output:
            return output
        return "No tasks"

    def complete_task(self, task_id: int) -> str | None:
        if task_id not in self.tasks:
            return "Task not found"
        self.tasks.pop(task_id)
        return None

    def delete_task(self, task_id: int) -> str | None:
        if task_id not in self.tasks:
            return "Task not found"
        self.tasks.pop(task_id)
        return None
