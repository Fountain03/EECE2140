import tkinter as tk
from View.task_view import TaskView
from Model.meeting import Meeting
from View.meeting_view import MeetingView
from View.reminder_view import ReminderView
from Model.reminder import Reminder


class DailyView():

    def __init__(self, day) -> None:
        self.day = day
        self.disp = tk.Toplevel()
        self.disp.title(f'Daily View: {self.day.date}')

    def display(self):

        for t in self.day.tasks:
            self.task_list(t)

    def task_list(self, task):
        def complete():
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
            if isinstance(task, Meeting):
                tv = MeetingView(task)
                tv.edit()
            if isinstance(task, Reminder):
                tv = ReminderView(task)
                tv.edit()
        t_button['command'] = edit

        t_button.pack(side=tk.RIGHT)
        f.pack()
