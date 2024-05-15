import json
import os

class ToDoList:
    def __init__(self, filename='to_do_list.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task['done'] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            self.save_tasks()
        else:
            print("Invalid task index")

    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            self.save_tasks()
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
        else:
            print("Invalid task index")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task index to mark as done: ")) - 1
            todo_list.mark_task_done(task_index)
        elif choice == '5':
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
