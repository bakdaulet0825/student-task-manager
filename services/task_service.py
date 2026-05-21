import json


class TaskService:

    def __init__(self):

        self.filename = "data/tasks.json"

        self.tasks = []

    def add_task(self, title, description):

        new_task = {
            "title": title,
            "description": description,
            "completed": False
        }

        self.tasks.append(new_task)

        self.save_tasks()

    def save_tasks(self):

        with open(self.filename, "w") as file:

            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):

        try:

            with open(self.filename, "r") as file:

                self.tasks = json.load(file)

        except:

            self.tasks = []

    def delete_task(self, index):

        if 0 <= index < len(self.tasks):

            del self.tasks[index]

            self.save_tasks()

    def complete_task(self, index):

        if 0 <= index < len(self.tasks):

            self.tasks[index]["completed"] = True

            self.save_tasks()

    def update_task(self, index, title, description):

        if 0 <= index < len(self.tasks):

            self.tasks[index]["title"] = title
            self.tasks[index]["description"] = description

            self.save_tasks()