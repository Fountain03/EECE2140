import tkinter as tk
from View.task_view import TaskView
from Model.meeting import Meeting
from Model.todo import ToDo
from Model.planner import Calendar
from View.meeting_view import MeetingView
from View.reminder_view import ReminderView
from Model.reminder import Reminder
from View.todo_view import ToDoView
import pickle


class DailyView():
    """This class represents a GUI display for a given Day"""

    def __init__(self, day, cal, dat) -> None:
        """Create a GUI object for day view

        Args:
            day (Day): the day to display
            cal (Calendar): the calendar being used
            dat (str): the file to save data to
        """
        self.day = day
        self.disp = tk.Tk()
        self.disp.title(f'Daily View: {self.day.date}')
        self.cal = cal
        self.dat = dat

    def display(self):
        """Display the tasks in the given day"""
        if len(self.day.tasks) == 0:
            msg = tk.Label(self.disp, text='No tasks for today!')
            msg.pack()

        for t in self.day.tasks:
            self.task_list(t)
        self.disp.mainloop()

    def task_list(self, task):
        """For a given task, display a button which will allow for editing
            and a checkbox to mark as complete and remove it

        Args:
            task (Task): a given task
        """
        def complete():
            """If a checkbox is marked, make the task done and remove it
                from the calendar"""
            if var.get() == 1:
                task.make_done()
            else:
                task.done == False
            self.day.remove_task(task)

        var = tk.IntVar()
        f = tk.Frame(self.disp)
        c = tk.Checkbutton(master=f, text='Completed', variable=var, onvalue=1, offvalue=0,
                           command=complete)
        c.pack(side=tk.LEFT)
        t_button = tk.Button(master=f, text=str(task))

        def edit():
            """If a button is clicked, allow the user to modify the task
                information"""
            if isinstance(task, Meeting):
                tv = MeetingView(task)
                tv.edit(t_button, self.cal)
            if isinstance(task, Reminder):
                tv = ReminderView(task)
                tv.edit(t_button, self.cal)
            if isinstance(task, ToDo):
                tv = ToDoView(task)
                tv.edit(t_button, self.cal)
            with open(self.dat, 'wb') as f:
                pickle.dump(self.cal, f)

        t_button['command'] = edit
        t_button.pack(side=tk.RIGHT)
        f.pack()
