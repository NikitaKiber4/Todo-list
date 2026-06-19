import core.tasks as tasks

def main():
    tasker = tasks.Task()
    controller(tasker)

def controller(tasker):
    while True:
        options = ("1", "2", "3", "4")
        print("Choose one option:\nAdd task[1]\nShow tasks[2]\nComplete task[3]\nDelete task[4]\nExit[5]")
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
            for tsk in output:
                if len(tsk) == 4:
                    print(f"[{tsk[0]}]{tsk[1]}\nTask: {tsk[2]}\nDescription: {tsk[3]}")
                else:
                    print(f"[{tsk[0]}]{tsk[1]}\nTask: {tsk[2]}")
                print()

        elif option == "3":
            try:
                inp = int(input("Enter task id: "))
            except ValueError:
                print("Invalid task id\n")
                return controller(tasker)
            err = tasker.complete_task(inp)
            if err:
                print(err)

        else:
            try:
                inp = int(input("Enter task id: "))
            except ValueError:
                print("Invalid task id\n")
                return controller(tasker)
            err = tasker.delete_task(inp)
            if err:
                print(err)

        print()

if __name__ == "__main__":
    main()
