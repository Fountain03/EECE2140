import datetime
from Model.task import Task
from Model.date import Date


class Calendar:
    """This class represents a calendar that can store events"""

    def __init__(self) -> None:
        """Creates a Calendar object"""
        self.dates = {}

    def add_task(self, task: Task):
        """Adds the given task to the calendar

        Args:
            task (Task): a Task object to be shown in the calendar
        """
        if task.date in self.dates:
            self.dates[task.date].add_task(task)
        else:
            self.dates[task.date] = Date(task.date)
            self.dates[task.date].add_task(task)

    def get_date(self, date):
        if date in self.dates:
            return self.dates[date]
        else:
            self.dates[date] = Date(date)
            return self.dates[date]

    def print_day(self, date):
        print(self.dates[date])

    def print_tasks(self) -> str:
        for d in self.dates.values():
            print(d)

    def sort_dates(self):
        return sorted(self.dates)

    def today(self):
        return self.dates[datetime.date.today()]

    def update(self):
        for d in self.dates.values():
            for t in d.tasks:
                if t.date != d.date:
                    d.remove_task(t)
