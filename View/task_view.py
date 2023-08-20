import tkinter as tk
from Model.meeting import Meeting
from abc import ABC, abstractmethod


class TaskView(ABC):

    def __init__(self, task) -> None:
        self.task = task
        self.disp = tk.Toplevel()
        self.disp.title('Edit task')

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    def add_task(self, cal):
        cal.add_task(self.task)
