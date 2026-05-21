from models.task import Task

class ImportantTask(Task):
    def __init__(self, title, description, priority):
        super().__init__(title, description)
        self.priority = priority

    def to_dict(self):
        data = super().to_dict()
        data["priority"] = self.priority
        return data