from Model.month import Month
from Model.day import Day


class Year:
    """This class represents a year in a calendar"""

    def __init__(self, year) -> None:
        """Creates a Year object with the given year number

        Args:
            year (int): the year to create
        """
        self.year = year
        self.months = {x: Month(x) for x in range(1, 13)}
        if (self.year % 4 == 0 and self.year % 100 != 0) or \
                self.year % 400 == 0:
            self.months[2].days[29] = Day(29)

    def get_month(self, month):
        """Given a month, returns that month in this year

        Args:
            month (int): the month to return

        Returns:
            Month: the Month object which correlates to the given int
        """
        return self.months[month]

    def add_task(self, task):
        """Adds the given task to this year

        Args:
            task (Task): the Task to add to this year
        """
        self.get_month(task.get_month()).add_task(task)

    def update(self, task):
        """Updates to remove the given task in this year

        Args:
            task (Task): the completed task to remove
        """
        for m in self.months.values():
            m.update(task)

    def __str__(self) -> str:
        s = ''
        for m, month in self.months.items():
            s += f'{m}/{self.year}\n{str(month)}'
        return s
