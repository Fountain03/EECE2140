from task import Task


class ToDo(Task):
    """This class represents a to do task for a calendar"""

    def __init__(self, title: str, year, month, day, desc) -> None:
        """Creates a ToDo task with a title, description and due date

        Args:
            title (str): title of the task
            year (int): year of the due date
            month (int): month of the due date
            day (int): day of the due date
            desc (str): description of the due date
        """
        super().__init__(title, year, month, day)
        self.desc = desc
