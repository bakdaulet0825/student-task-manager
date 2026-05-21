import tkinter as tk
from tkinter import messagebox
from services.task_service import TaskService


class TaskManagerApp:

    def __init__(self):
        self.service = TaskService()

        self.window = tk.Tk()
        self.window.title("Student Task Manager")
        self.window.geometry("700x500")

        self.title_label = tk.Label(
            self.window,
            text="Task Title"
        )
        self.title_label.pack()

        self.title_entry = tk.Entry(
            self.window,
            width=50
        )
        self.title_entry.pack()

        self.description_label = tk.Label(
            self.window,
            text="Description"
        )
        self.description_label.pack()

        self.description_entry = tk.Entry(
            self.window,
            width=50
        )
        self.description_entry.pack()

        self.add_button = tk.Button(
            self.window,
            text="Add Task",
            command=self.add_task
        )
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(
            self.window,
            text="Update Task",
            command=self.update_task
        )
        self.update_button.pack(pady=5)

        self.complete_button = tk.Button(
            self.window,
            text="Complete Task",
            command=self.complete_task
        )
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(
            self.window,
            text="Delete Task",
            command=self.delete_task
        )
        self.delete_button.pack(pady=5)

        self.task_listbox = tk.Listbox(
            self.window,
            width=90,
            height=15
        )
        self.task_listbox.pack(pady=10)

        self.refresh_tasks()

    def add_task(self):

        title = self.title_entry.get()
        description = self.description_entry.get()

        if not title or not description:

            messagebox.showwarning(
                "Warning",
                "Please fill all fields"
            )

            return

        self.service.add_task(title, description)

        print("TASK ADDED")

        self.refresh_tasks()

        self.clear_entries()

    def delete_task(self):
        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a task"
            )
            return

        self.service.delete_task(selected[0])

        self.refresh_tasks()

    def complete_task(self):
        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a task"
            )
            return

        self.service.complete_task(selected[0])

        self.refresh_tasks()

    def update_task(self):
        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a task"
            )
            return

        title = self.title_entry.get()
        description = self.description_entry.get()

        self.service.update_task(
            selected[0],
            title,
            description
        )

        self.refresh_tasks()
        self.clear_entries()

    def refresh_tasks(self):

        self.task_listbox.delete(0, tk.END)

        for task in self.service.tasks:

            status = (
                "Done"
                if task["completed"]
                else "Pending"
            )

            self.task_listbox.insert(
                tk.END,
                f"{task['title']} | "
                f"{task['description']} | "
                f"{status}"
            )
    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()