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
        """Return a specific Date object

        Args:
            date (datetime): the desired date

        Returns:
            Date: Date object with given date
        """
        if date in self.dates:
            return self.dates[date]
        else:
            self.dates[date] = Date(date)
            return self.dates[date]

    def today(self):
        """Return the Date object for today's date

        Returns:
            Date: Date object for today
        """
        return self.dates[datetime.date.today()]

    def update(self):
        """If tasks in any date do not have the matching date, 
            remove them from that Date
        """
        for d in self.dates.values():
            d.update()
