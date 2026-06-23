import core.tasks as tasks
from fastapi import FastAPI, HTTPException
from core.models import CreateTask

app = FastAPI(title="Todo List API")

tasker = tasks.TaskManager()
tasker.add_task("task")

@app.get("/api/v1/tasks")
async def get_tasks(is_completed: bool | None = None):
    task_list = []
    output = tasker.list_tasks()

    for task_id, task_obj in output.items():
        task_is_completed = task_obj.status == "Completed"

        if is_completed == task_is_completed or is_completed is None:
            task_list.append({
                "id": task_id,
                 "created_at": task_obj.created_at,
                 "status": task_obj.status,
                 "title": task_obj.title,
                 "description": task_obj.description
                 })
    return task_list


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: int):
    output = tasker.list_tasks()
    try:
        task_obj = output[task_id]
        return {
            "id": task_id,
             "created_at": task_obj.created_at,
             "status": task_obj.status,
             "title": task_obj.title,
             "description": task_obj.description
             }
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.post("/api/v1/tasks")
async def create_task(task_in: CreateTask):
    title = task_in.title
    description = task_in.description

    tasker.add_task(title, description)
    return {"message": "Task created successfully", "task": task_in}


@app.put("/api/v1/tasks/{task_id}")
async def complete_task(task_id: int):
    task_list = tasker.list_tasks()

    if task_id not in task_list:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_list[task_id].status == "Completed":
        raise HTTPException(status_code=409, detail="Task already completed")

    tasker.complete_task(task_id)
    return {"message": "Task completed successfully"}


@app.delete("/api/v1/tasks/{task_id}")
async def delete_task(task_id: int):
    task_list = tasker.list_tasks()

    if task_id not in task_list:
        raise HTTPException(status_code=404, detail="Task not found")

    tasker.delete_task(task_id)
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
