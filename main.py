import core.tasks as tasks

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
                    if tsk[1].description:
                        print(f"[{tsk[0]}]{tsk[1].created_at}\nStatus: {tsk[1].status}\nTask: {tsk[1].title}\nDescription: {tsk[1].description}")
                    else:
                        print(f"[{tsk[0]}]{tsk[1].created_at}\nStatus: {tsk[1].status}\nTask: {tsk[1].title}")
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
