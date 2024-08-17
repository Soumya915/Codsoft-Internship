# To Do List

import os
import json

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, task_id, new_task):
        for i, task in enumerate(self.tasks):
            if i == task_id:
                self.tasks[i] = new_task
                self.save_tasks()
                break

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if i == task_id:
                del self.tasks[i]
                self.save_tasks()
                break

    def list_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

def main():
    filename = "todo_list.json"
    todo_list = TodoList(filename)

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter the task ID to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_id, new_task)
        elif choice == "3":
            task_id = int(input("Enter the task ID to delete: ")) - 1
            todo_list.delete_task(task_id)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()