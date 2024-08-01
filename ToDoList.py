import tkinter as tk
from tkinter import messagebox
import json
import os


class ToDoApp:
    def __init__(self,root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = self.load_tasks()

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_tasks, fg="blue")
        self.add_btn.pack(pady=5)

        self.complete_btn = tk.Button(root, text="Mark as Completed", command=self.mark_completed, fg="magenta")
        self.complete_btn.pack(pady=5)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task, fg="red")
        self.delete_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=self.root.quit, fg="green")
        self.exit_btn.pack(pady=5)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for i,task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "✗"
            self.listbox.insert(tk.END, f"{i+1}. [{status}] {task['description']}")

    def add_tasks(self):
        description = self.entry.get().strip()
        if description:
            self.tasks.append({"description": description, "completed": False})
            self.entry.delete(0, tk.END)
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def mark_completed(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]['completed'] = True
            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as completed.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
