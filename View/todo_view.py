from Model.todo import ToDo
from View.task_view import TaskView
import tkinter as tk
import datetime


class ToDoView(TaskView):

    def __init__(self, task) -> None:
        super().__init__(task)

    def create(self, cal):
        f1 = tk.Frame(self.disp)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(self.disp)
        date_label = tk.Label(master=f2, text='Date D/M/YYYY')
        date_label.pack(side=tk.LEFT)
        month_entry = tk.Entry(master=f2, width=2)
        day_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)

        f3 = tk.Frame(self.disp)
        desc_label = tk.Label(master=f3, text='Description')
        desc_label.pack(side=tk.LEFT)
        desc_entry = tk.Entry(master=f3)
        desc_entry.pack(side=tk.RIGHT)

        f1.pack()
        f2.pack()
        f3.pack()

        def accept():
            title = title_entry.get()
            desc = desc_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            todo = ToDo(title, year, month, day, desc)
            cal.add_task(todo)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='add',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)

    def edit(self):
        f1 = tk.Frame(self.disp)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.insert(0, self.task.title)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(self.disp)
        date_label = tk.Label(master=f2, text='Date D/M/YYYY')
        date_label.pack(side=tk.LEFT)
        day_entry = tk.Entry(master=f2, width=2)
        month_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        day_entry.insert(0, self.task.date.day)
        month_entry.insert(0, self.task.date.month)
        year_entry.insert(0, self.task.date.year)
        day_entry.pack(side=tk.LEFT)
        month_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)

        f3 = tk.Frame(self.disp)
        desc_label = tk.Label(master=f3, text='Description')
        desc_label.pack(side=tk.LEFT)
        desc_entry = tk.Entry(master=f3)
        desc_entry.insert(0, self.task.desc)
        desc_entry.pack(side=tk.RIGHT)

        f1.pack()
        f2.pack()
        f3.pack()

        def accept():
            self.task.title = title_entry.get()
            self.task.desc = desc_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            self.task.date = datetime.date(year, month, day)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='add',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)
