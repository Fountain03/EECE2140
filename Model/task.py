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

    def __str__(self) -> str:
        """Return a string containing information about the task

        Returns:
            str: String with title of the task
        """
        return f'{self.title}\n'\


    def make_done(self):
        """Make this task marked as done"""
        self.done = True
