import core.repository.tasks as tasks
from fastapi import FastAPI, HTTPException, Depends
from core.models import CreateTask
from sqlalchemy.orm import Session
from core.database import get_db, engine, Base


app = FastAPI(title="Todo List API")
Base.metadata.create_all(bind=engine)

tasker = tasks.TaskManager()

@app.get("/api/v1/tasks")
async def get_tasks(is_completed: bool | None = None, db_session: Session = Depends(get_db)):
    db_tasks = tasker.list_tasks(db_session)
    task_list = []

    for task_obj in db_tasks:
        if is_completed == task_obj.status or is_completed is None:
            task_list.append({
                "id": task_obj.id,
                "created_at": task_obj.created_at,
                "status": "Completed" if task_obj.status else "Not Completed",
                "title": task_obj.title,
                "description": task_obj.description
            })

    return task_list


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: int, db_session: Session = Depends(get_db)):
    task_obj = tasker.list_tasks(db_session, task_id)

    if task_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task_id,
        "created_at": task_obj.created_at,
        "status": task_obj.status,
        "title": task_obj.title,
        "description": task_obj.description
    }


@app.post("/api/v1/tasks")
async def create_task(task_in: CreateTask, db_session: Session = Depends(get_db)):
    title = task_in.title
    description = task_in.description

    try:
        new_task = tasker.add_task(db_session, title, description)
    except Exception as e:
        print(f"Task creation failed: {e}")
        raise HTTPException(status_code=400, detail=f"Ошибка записи задачи в базу данных")
    return {"message": "Task created successfully", "task": {
        "id": new_task.id,
        "created_at": new_task.created_at,
        "status": new_task.status,
        "title": new_task.title,
        "description": new_task.description
    }}


@app.put("/api/v1/tasks/{task_id}")
async def complete_task(task_id: int, db_session: Session = Depends(get_db)):
    task = tasker.list_tasks(db_session, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status:
        raise HTTPException(status_code=409, detail="Task already completed")

    task = tasker.mark_as_completed(db_session, task)
    return {"message": "Task completed successfully", "task": {
        "id": task.id,
        "created_at": task.created_at,
        "status": task.status,
        "title": task.title,
        "description": task.description
    }}


@app.delete("/api/v1/tasks/{task_id}")
async def delete_task(task_id: int, db_session: Session = Depends(get_db)):
    task = tasker.list_tasks(db_session, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    tasker.delete_task(db_session, task)
    return {"message": "Task deleted successfully"}

def main():
    tasker = tasks.TaskManager()
    controller(tasker)

def controller(tasker):
    while True:
        options = ("1", "2", "3", "4")
        print("Choose one option:\nAdd task[1]\nShow tasks[2]\nComplete task[3]\nDelete task[4]")
        option = input("-->")
        print()

        if option not in options:
            print("Invalid option\n")

        elif option == "1":
            print("Write your task below. Press Enter and write description if needed.")
            task = input("Task: ")
            description = input("Description: ")
            tasker.add_task(task, description)

        elif option == "2":
            print("Task list:\n")
            output = tasker.list_tasks()
            if not output:
                print("No tasks found\n")
            else:
                for tsk in output:
                    if output[tsk].description:
                        print(f"[{tsk}]{output[tsk].created_at}\nStatus: {output[tsk].status}\nTask: {output[tsk].title}\nDescription: {output[tsk].description}")
                    else:
                        print(f"[{tsk}]{output[tsk].created_at}\nStatus: {output[tsk].status}\nTask: {output[tsk].title}")
                    print()

        elif option == "3":
            try:
                inp = int(input("Enter task id: "))

                tasker.complete_task(inp)
                print("Task completed successfully\n")
            except ValueError:
                print("Invalid task id\n")
            except tasks.TaskNotFoundError:
                print("Task not found\n")

        else:
            try:
                inp = int(input("Enter task id: "))

                tasker.delete_task(inp)
                print("Task deleted successfully\n")
            except ValueError:
                print("Invalid task id\n")
            except tasks.TaskNotFoundError:
                print("Task not found\n")
        print()

if __name__ == "__main__":
    main()
