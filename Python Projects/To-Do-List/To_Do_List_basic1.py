import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import the required modules from Pillow
import json
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.filename = 'to_do_list.json'
        self.load_tasks()

        self.create_widgets()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def resize_image(self, image_path, size):
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_icon = self.resize_image("images/add.png", (50, 50))
        self.add_task_button = tk.Button(self.root, image=self.add_task_icon, text="Add Task", compound="left", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Update Task Button
        self.update_task_icon = self.resize_image("images/update1.png", (50, 50))
        self.update_task_button = tk.Button(self.root, image=self.update_task_icon, text="Update Task", compound="left", command=self.update_task)
        self.update_task_button.pack(pady=5)

        # Mark Task as Done Button
        self.mark_done_icon = self.resize_image("images/done.png", (50, 50))
        self.mark_done_button = tk.Button(self.root, image=self.mark_done_icon, text="Mark Done", compound="left", command=self.mark_task_done)
        self.mark_done_button.pack(pady=5)

        # Delete Task Button
        self.delete_task_icon = self.resize_image("images/delete.png", (50, 50))
        self.delete_task_button = tk.Button(self.root, image=self.delete_task_icon, text="Delete Task", compound="left", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.load_tasks_to_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.save_tasks()
            self.load_tasks_to_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['done'] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                index = selected_task_index[0]
                self.tasks[index]["task"] = new_task
                self.save_tasks()
                self.load_tasks_to_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def mark_task_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["done"] = True
            self.save_tasks()
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.save_tasks()
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    
    root.geometry("400x650+400+100")
    root.resizable(False,False)

    
    # Window Icon
    window_icon = ImageTk.PhotoImage(file="images/todolist1.png")
    root.iconphoto(False, window_icon)
    root.mainloop()
