import datetime
from Model.month import Month
from Model.day import Day
from Model.year import Year
from Model.task import Task


class Calendar:
    """This class represents a calendar that can store events"""

    def __init__(self) -> None:
        """Creates a Calendar object"""
        self.years = {}

    def get_year(self, year: int):
        """Given a year int, returns the Year object

        Args:
            year (int): the year to return

        Returns:
            Year: The year in the calendar
        """
        if year not in self.years:
            raise ValueError('Nothing planned for year')
        return self.years[year]

    def add_task(self, task: Task):
        """Adds the given task to the calendar

        Args:
            task (Task): a Task object to be shown in the calendar
        """
        if task.get_year() in self.years:
            self.get_year(task.get_year()).add_task(task)
        else:
            self.years[task.get_year()] = Year(task.get_year())
            self.get_year(task.get_year()).add_task(task)

    def update(self, task):
        """Updates the given task to be complete

        Args:
            task (_type_): a Task object which has been 
            completed by the user
        """
        task.make_done()
        for y in self.years:
            y.update(task)
