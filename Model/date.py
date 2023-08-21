import datetime
from Model.task import Task


class Date:
    """This class represents a specific Date in the year"""

    def __init__(self, date) -> None:
        """Creates a Date object

        Args:
            date (datetime): year, month and day
        """
        self.date = date
        self.tasks = []

    def add_task(self, task):
        """Add a task to this day

        Args:
            task (Task): a Task of importance
        """
        self.tasks.append(task)

    def remove_task(self, task):
        """Remove the given task from this day

        Args:
            task (Task): task to remove
        """
        self.tasks.remove(task)

    def update(self):
        """If any tasks in this Day have a different date, remove them"""
        for t in self.tasks:
            if t.date != self.date:
                self.tasks.remove(t)

    def __str__(self):
        """Return a string with notation for the date and list of tasks

        Returns:
            str: string with date and tasks
        """
        s = f'{str(self.date)}\n'
        if self.tasks == {}:
            return s + 'No tasks today!'
        else:
            for t in self.tasks:
                s += str(t) + '\n'
            return s
