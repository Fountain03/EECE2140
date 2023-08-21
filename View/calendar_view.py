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
    """This class represents the view for a Calendar"""

    def __init__(self, cal, dat='cal.dat') -> None:
        """Creates a Calendar View object

        Args:
            cal (Calendar): the Calendar to display
            dat (str, optional): the file to save to. 
                                 Defaults to 'cal.dat'.
        """
        self.cal = cal
        self.dat = dat
        self.page = tk.Tk()
        self.page.title(f'Calendar: saved to {self.dat}')
        self.page.geometry('500x300')

    def daily_view(self):
        """Creates a view for the day"""
        new = tk.Toplevel()
        f1 = tk.Frame(new)
        # Ask the user for date to display
        date_label = tk.Label(master=f1, text='Date M/D/YYYY')
        date_label.pack(side=tk.LEFT)
        month_entry = tk.Entry(master=f1, width=2)
        day_entry = tk.Entry(master=f1, width=2)
        year_entry = tk.Entry(master=f1, width=4)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()

        # Create display for given day
        def accept():
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            d = datetime.date(year, month, day)
            date = self.cal.get_date(d)
            dv = DailyView(date, self.cal, self.dat)
            dv.display()
        search = tk.Button(new, text='search',
                           command=accept)
        search.pack(side=tk.BOTTOM)

    def new_remind(self):
        """Create a new reminder and add to calendar"""
        rv = ReminderView(None)
        rv.create(self.cal)
        with open(self.dat, 'wb') as f:
            pickle.dump(self.cal, f)

    def new_meeting(self):
        """Create a new meeting and add to calendar"""
        mv = MeetingView(None)
        mv.create(self.cal)
        with open(self.dat, 'wb') as f:
            pickle.dump(self.cal, f)

    def new_todo(self):
        """Create a new ToDo and add to calendar"""
        tv = ToDoView(None)
        tv.create(self.cal)
        with open(self.dat, 'wb') as f:
            pickle.dump(self.cal, f)

    def menu(self):
        """Display menu with options for user to do with calendar"""
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
                          command=lambda: DailyView(
                              self.cal.get_date(td),
                              self.cal, self.dat).display())
        remind.pack()
        todo.pack()
        meeting.pack()
        daily.pack()
        today.pack()
        self.page.mainloop()
