import datetime
from abc import ABC


class Task(ABC):
    """This class represents a task/event to be shown on the calendar"""

    def __init__(self, title: str, year, month, day) -> None:
        """Creates a Task object with a title and date

        Args:
            title (str): The title of the task/event
            year (int): the year the task occurs
            month (int): the month the task occurs
            day (int): the day the task occurs
        """
        self.title = title
        self.date = datetime.date(year, month, day)
        self.done = False

    def get_day(self):
        """Returns the task's day of occurrence

        Returns:
            int: the day the task is assigned to
        """
        return self.date.day

    def get_month(self):
        """Returns the task's month of occurrence

        Returns:
            int: the month the task is assigned to
        """
        return self.date.month

    def get_year(self):
        """Returns the task's year of occurrence

        Returns:
            int: the year the task is assigned to
        """
        return self.date.year

    def __str__(self) -> str:
        return f'{self.title}\n'\


    def make_done(self):
        self.done = True
