import datetime
import tkinter as tk
from Model.task import Task
from Model.planner import Calendar
from Model.reminder import Reminder
from Model.todo import ToDo
from Model.meeting import Meeting
from View.meeting_view import MeetingView
from View.daily_view import DailyView
from View.reminder_view import ReminderView
from View.todo_view import ToDoView
import pickle


class CalendarView():

    def __init__(self, cal) -> None:
        self.cal = cal
        self.page = tk.Tk()
        self.page.title('Calendar View')
        self.page.geometry('500x300')

    def daily_view(self):
        new = tk.Toplevel()
        f1 = tk.Frame(new)
        date_label = tk.Label(master=f1, text='Date M/D/YYYY')
        date_label.pack(side=tk.LEFT)
        month_entry = tk.Entry(master=f1, width=2)
        day_entry = tk.Entry(master=f1, width=2)
        year_entry = tk.Entry(master=f1, width=4)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()

        def accept():
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            d = datetime.date(year, month, day)
            date = self.cal.dates[d]
            dv = DailyView(date)
            dv.display()
        search = tk.Button(new, text='search',
                           command=accept)
        search.pack(side=tk.BOTTOM)

    def new_remind(self):
        rv = ReminderView(None)
        rv.create(self.cal)
        with open('cal.dat', 'wb') as f:
            pickle.dump(self.cal, f)

    def new_meeting(self):
        mv = MeetingView(None)
        mv.create(self.cal)
        with open('cal.dat', 'wb') as f:
            pickle.dump(self.cal, f)

    def new_todo(self):
        tv = ToDoView(None)
        tv.create(self.cal)
        with open('cal.dat', 'wb') as f:
            pickle.dump(self.cal, f)

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
        today = tk.Button(text='Today', height=3, width=15,
                          command=lambda: DailyView(self.cal.get_date(td)).display())
        remind.pack()
        todo.pack()
        meeting.pack()
        daily.pack()
        today.pack()

        def on_close():

            self.page.destroy()
        self.page.protocol('WM_DELETE_WINDOW', on_close)
        self.page.mainloop()
