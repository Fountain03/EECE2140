import tkinter as tk
from Model.meeting import Meeting
from abc import ABC, abstractmethod


class TaskView(ABC):
    """This class is an abstract class for GUIs for a view"""

    def __init__(self, task) -> None:
        """Creates a TaskView object

        Args:
            task (Task): the given task
        """
        self.task = task
        self.disp = tk.Toplevel()
        self.disp.title('Edit task')

    @abstractmethod
    def create(self):
        """Allows the user to create a task and add it to the calendar"""
        pass

    @abstractmethod
    def edit(self):
        """Allows the user to edit a task"""
        pass
