class Day:
    """This class represents a day in a year"""

    def __init__(self, date) -> None:
        """Creates a Day object

        Args:
            date (int): what number day of the month the day is
        """
        self.date = date
        self.tasks = {}

    def add_task(self, task):
        """Adds the given task to the day

        Args:
            task (Task): a task to be shown on this Day
        """
        self.tasks[task.title] = task

    def get_tasks(self):
        """Returns this day's list of tasks

        Returns:
            list[Tasks]: the tasks that are assigned on this day
        """
        return self.tasks.values

    def update(self, task):
        """Given a task, removes the task from the list

        Args:
            task (Task): the completed task to remove
        """
        if task.title in self.tasks:
            if task.done:
                del self.tasks[task]
