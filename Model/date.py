import datetime
from Model.task import Task


class Date:

    def __init__(self, date) -> None:
        self.date = date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task.done:
            self.tasks.remove(task)

    def __str__(self):
        s = f'{str(self.date)}\n'
        for t in self.tasks:
            s += str(t) + '\n'
        return s
