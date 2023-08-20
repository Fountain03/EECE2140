from Model.meeting import Meeting
from View.task_view import TaskView
import tkinter as tk
import datetime


class MeetingView(TaskView):

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

        f3 = tk.Frame(self.disp)
        desc_label = tk.Label(master=f3, text='Description')
        desc_label.pack(side=tk.LEFT)
        desc_entry = tk.Entry(master=f3)
        desc_entry.pack(side=tk.RIGHT)

        f4 = tk.Frame(self.disp)
        loc_label = tk.Label(master=f4, text='Location')
        loc_label.pack(side=tk.LEFT)
        loc_entry = tk.Entry(master=f4)
        loc_entry.pack(side=tk.RIGHT)

        f5 = tk.Frame(self.disp)
        time_label = tk.Label(master=f5, text='Start Time XX:XX')
        time_label.pack(side=tk.LEFT)
        time_entry = tk.Entry(master=f5)
        time_entry.pack(side=tk.RIGHT)

        f6 = tk.Frame(self.disp)
        dur_label = tk.Label(master=f6, text='Duration in hrs')
        dur_label.pack(side=tk.LEFT)
        dur_entry = tk.Entry(master=f6)
        dur_entry.pack(side=tk.RIGHT)

        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        f5.pack()
        f6.pack()

        def accept():
            dur = int(dur_entry.get())
            time = time_entry.get()
            desc = desc_entry.get()
            loc = loc_entry.get()
            title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            self.task = Meeting(title, year, month, day, desc, dur, loc, time)
            cal.add_task(self.task)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='save',
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
        date_label = tk.Label(master=f2, text='Date M/D/YYYY')
        date_label.pack(side=tk.LEFT)
        month_entry = tk.Entry(master=f2, width=2)
        day_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        day_entry.insert(0, self.task.date.day)
        month_entry.insert(0, self.task.date.month)
        year_entry.insert(0, self.task.date.year)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)

        f3 = tk.Frame(self.disp)
        desc_label = tk.Label(master=f3, text='Description')
        desc_label.pack(side=tk.LEFT)
        desc_entry = tk.Entry(master=f3)
        desc_entry.insert(0, self.task.desc)
        desc_entry.pack(side=tk.RIGHT)

        f4 = tk.Frame(self.disp)
        loc_label = tk.Label(master=f4, text='Location')
        loc_label.pack(side=tk.LEFT)
        loc_entry = tk.Entry(master=f4)
        loc_entry.insert(0, self.task.loc)
        loc_entry.pack(side=tk.RIGHT)

        f5 = tk.Frame(self.disp)
        time_label = tk.Label(master=f5, text='Start Time XX:XX')
        time_label.pack(side=tk.LEFT)
        time_entry = tk.Entry(master=f5)
        time_entry.insert(0, self.task.start)
        time_entry.pack(side=tk.RIGHT)

        f6 = tk.Frame(self.disp)
        dur_label = tk.Label(master=f6, text='Duration in hrs')
        dur_label.pack(side=tk.LEFT)
        dur_entry = tk.Entry(master=f6)
        dur_entry.insert(0, self.task.duration)
        dur_entry.pack(side=tk.RIGHT)

        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        f5.pack()
        f6.pack()

        def accept():
            self.task.duration = int(dur_entry.get())
            self.task.start = time_entry.get()
            self.task.desc = desc_entry.get()
            self.task.loc = loc_entry.get()
            self.task.title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            self.task.date = datetime.date(year, month, day)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='save',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)
        self.disp.mainloop()
