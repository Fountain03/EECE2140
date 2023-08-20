import datetime
from Model.task import Task


class Date:

    def __init__(self, date) -> None:
        self.date = date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def update(self):
        for t in self.tasks:
            if t.date != self.date:
                self.tasks.remove(t)

    def __str__(self):
        s = f'{str(self.date)}\n'
        if self.tasks == {}:
            return s + 'No tasks today!'
        else:
            for t in self.tasks:
                s += str(t) + '\n'
            return s
