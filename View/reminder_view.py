from Model.reminder import Reminder
from View.task_view import TaskView
import tkinter as tk
import datetime


class ReminderView(TaskView):

    def __init__(self, task) -> None:
        super().__init__(task)

    def create(self, cal):
        f1 = tk.Frame(self.disp)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(self.disp)
        date_label = tk.Label(master=f2, text='Date M/D/YYYY')
        date_label.pack(side=tk.LEFT)
        day_entry = tk.Entry(master=f2, width=2)
        month_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()
        f2.pack()

        def accept():
            title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            self.task = Reminder(title, year, month, day)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='save',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)

    def edit(self, button):
        f1 = tk.Frame(self.disp)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.insert(0, self.task.title)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(self.disp)
        date_label = tk.Label(master=f2, text='Date M/D/YYYY')
        date_label.pack(side=tk.LEFT)
        month_entry = tk.Entry(master=f2, width=2)
        day_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        month_entry.insert(0, self.task.date.month)
        year_entry.insert(0, self.task.date.year)
        day_entry.insert(0, self.task.date.day)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()
        f2.pack()

        def accept():
            self.task.title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            self.task.date = datetime.date(year, month, day)
            button['text'] = str(self.task)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='save',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)
