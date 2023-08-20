from Model.meeting import Meeting
from Model.todo import ToDo
from Model.planner import Calendar
from Model.reminder import Reminder
from View.calendar_view import CalendarView
from Model.date import Date
from View.daily_view import DailyView
from View.meeting_view import MeetingView
import pickle
import datetime
import tkinter as tk


c1 = Calendar()
m = Meeting('Interview', 2023, 8, 20, 'job interview', 3, 'Teams', '2:30')
r = Reminder('Make Dinner', 2023, 8, 20)
to = ToDo('Project', 2023, 8, 20, 'EECE2140 project')
day = datetime.date(2023, 8, 20)
date = Date(day)
date.add_task(m)
c1.add_task(m)
c1.add_task(to)
c1.add_task(r)
cv = CalendarView(c1)
cv.menu()
