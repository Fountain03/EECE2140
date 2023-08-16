import datetime
import tkinter as tk
from Model.month import Month
from Model.day import Day
from Model.year import Year
from Model.task import Task
from View.day_view import DayView
from Model.planner import Calendar
from Model.reminder import Reminder
from Model.todo import ToDo
from Model.meeting import Meeting
import pickle


class CalendarView():

    def __init__(self, cal) -> None:
        self.cal = cal
        self.page = tk.Tk()
        self.page.title('Calendar View')
        self.page.geometry('500x300')
        options = ['new reminder', 'new to do', 'new meeting',
                   'daily view', 'monthly view']

    def accept(self, year, month, day):
        target = self.cal.get_year(year).get_month(month).get_day(day)
        target_view = DayView(target)
        target_view.schedule()

    def daily_view(self):
        new_window = tk.Toplevel()
        f1 = tk.Frame(new_window)
        date_label = tk.Label(master=f1, text='Date D/M/YYYY')
        date_label.pack(side=tk.LEFT)
        day_entry = tk.Entry(master=f1, width=2)
        month_entry = tk.Entry(master=f1, width=2)
        year_entry = tk.Entry(master=f1, width=4)
        day_entry.pack(side=tk.LEFT)
        month_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()

        def accept():
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            new_window.destroy()
            self.accept(year, month, day)

        show = tk.Button(new_window, text='show day view',
                         command=accept)
        show.pack(side=tk.BOTTOM)

    def new_remind(self):
        new_window = tk.Toplevel()
        f1 = tk.Frame(new_window)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(new_window)
        date_label = tk.Label(master=f2, text='Date D/M/YYYY')
        date_label.pack(side=tk.LEFT)
        day_entry = tk.Entry(master=f2, width=2)
        month_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        day_entry.pack(side=tk.LEFT)
        month_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()
        f2.pack()

        def accept():
            title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            reminder = Reminder(title, year, month, day)
            self.cal.add_task(reminder)
            new_window.destroy()

        new_button = tk.Button(new_window, text='add',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)

    def new_meeting(self):
        new_window = tk.Toplevel()
        f1 = tk.Frame(new_window)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(new_window)
        date_label = tk.Label(master=f2, text='Date D/M/YYYY')
        date_label.pack(side=tk.LEFT)
        day_entry = tk.Entry(master=f2, width=2)
        month_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        day_entry.pack(side=tk.LEFT)
        month_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)

        f3 = tk.Frame(new_window)
        desc_label = tk.Label(master=f3, text='Description')
        desc_label.pack(side=tk.LEFT)
        desc_entry = tk.Entry(master=f3)
        desc_entry.pack(side=tk.RIGHT)

        f4 = tk.Frame(new_window)
        loc_label = tk.Label(master=f4, text='Location')
        loc_label.pack(side=tk.LEFT)
        loc_entry = tk.Entry(master=f4)
        loc_entry.pack(side=tk.RIGHT)

        f5 = tk.Frame(new_window)
        time_label = tk.Label(master=f5, text='Start Time XX:XX')
        time_label.pack(side=tk.LEFT)
        time_entry = tk.Entry(master=f5)
        time_entry.pack(side=tk.RIGHT)

        f6 = tk.Frame(new_window)
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
            meeting = Meeting(title, year, month, day, desc, dur, loc, time)
            self.cal.add_task(meeting)
            new_window.destroy()

        new_button = tk.Button(new_window, text='add',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)

    def new_todo(self):
        new_window = tk.Toplevel()
        f1 = tk.Frame(new_window)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.pack(side=tk.RIGHT)
        title = title_entry.get()

        f2 = tk.Frame(new_window)
        date_label = tk.Label(master=f2, text='Date')
        date_label.pack(side=tk.LEFT)
        day_entry = tk.Entry(master=f2, width=2)
        month_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        day_entry.pack(side=tk.LEFT)
        month_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)

        f3 = tk.Frame(new_window)
        desc_label = tk.Label(master=f3, text='Description')
        desc_label.pack(side=tk.LEFT)
        desc_entry = tk.Entry(master=f3)
        desc_entry.pack(side=tk.RIGHT)
        desc = desc_entry.get()

        f1.pack()
        f2.pack()
        f3.pack()

        def accept():
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            todo = ToDo(title, year, month, day, desc)
            self.cal.add_task(todo)
            new_window.destroy()

        new_button = tk.Button(new_window, text='add',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)

    def menu(self):
        td = datetime.date.today()
        remind = tk.Button(text='New Reminder',
                           height=3, width=15, command=self.new_remind)
        todo = tk.Button(text='New To Do', height=3,
                         width=15, command=self.new_todo)
        meeting = tk.Button(text='New Meeting', height=3, width=15,
                            command=self.new_meeting)
        daily = tk.Button(text='Day View', height=3,
                          width=15, command=self.daily_view)
        today = tk.Button(text='Today', height=3, width=15,  command=lambda: self.accept(
            td.year, td.month, td.day))
        remind.pack()
        todo.pack()
        meeting.pack()
        daily.pack()
        today.pack()

        def on_close():
            with open('cal.dat', 'wb') as f:
                pickle.dump(self.cal, f)
                self.page.destroy()
        self.page.protocol('WM_DELETE_WINDOW', on_close)
        self.page.mainloop()
