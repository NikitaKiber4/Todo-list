from datetime import datetime
from core.models import TaskModel
from sqlalchemy.orm import Session

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

    def add_task(self, db_session, title: str, description = None) -> TaskModel:
        now = datetime.now()
        created_at = now.strftime("%d.%m.%y %H:%M:%S")

        model = TaskModel(
            created_at = created_at,
            status = False,
            title = title,
            description = description
        )

        db_session.add(model)
        db_session.commit()
        db_session.refresh(model)
        return model

    def list_tasks(self, db_session, task_id: int = None):
        if task_id is not None:
            return db_session.query(TaskModel).filter(TaskModel.id == task_id).first()
        return db_session.query(TaskModel).all()

    def mark_as_completed(self, db_session, task) -> TaskModel:
        task.status = True
        db_session.commit()
        return task

    def delete_task(self, db_session, task) -> None:
        db_session.delete(task)
        db_session.commit()



class TaskNotFoundError(Exception):
    pass