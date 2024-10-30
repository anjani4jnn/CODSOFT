class Task:
    def __init__(self, title, description="", due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} - {status}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx + 1}. {task}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()


def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Mark Task Completed")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(Task(title, description))
            print(f"Task '{title}' added.")

        elif choice == "2":
            todo_list.list_tasks()
            task_index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(task_index)
            print("Task removed.")

        elif choice == "3":
            todo_list.list_tasks()

        elif choice == "4":
            todo_list.list_tasks()
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
            print("Task marked as completed.")

        elif choice == "5":
            print("Exiting the application.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
