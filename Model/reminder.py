from Model.task import Task


class Reminder(Task):
    """This class represents a reminder task for a calendar"""

    def __init__(self, title: str, year, month, day) -> None:
        """Creates a reminder with a title and date

        Args:
            title (str): title of the reminder
            year (int): year of the reminder
            month (int): month of the reminder
            day (int): day of the reminder
        """
        super().__init__(title, year, month, day)
