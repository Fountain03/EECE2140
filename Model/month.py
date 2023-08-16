import datetime
from Model.day import Day


class Month:
    """This class represents a month in a year"""

    def __init__(self, month) -> None:
        """Creates a Month object

        Args:
            month (int): the number month in the year
        """
        self.month = month
        self.tasks = {}
        if self.month == 4 or self.month == 6 or \
                self.month == 9 or self.month == 11:
            self.days = {x: Day(x) for x in range(1, 31)}
        elif self.month == 2:
            self.days = {x: Day(x) for x in range(1, 29)}
        else:
            self.days = {x: Day(x) for x in range(1, 32)}

    def get_day(self, day):
        """Returns the given Day object

        Args:
            day (int): the day to return

        Returns:
            Day: the Day object of the given day in this month
        """
        return self.days[day]

    def add_task(self, task):
        """Adds the given task to this month

        Args:
            task (Task): the Task to add to this month
        """
        self.get_day(task.get_day()).add_task(task)

    def update(self, task):
        """Updates this month with the given task's information

        Args:
            task (Task): the Task to update
        """
        for d in self.days.values():
            d.update(task)

    def __str__(self) -> str:
        s = ''
        for d, day in self.days.items():
            if bool(day.get_tasks()):
                s += f'{self.month}/{d}: \n{str(day)}'
        return s
