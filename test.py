from Model.meeting import Meeting
from Model.todo import ToDo
from Model.planner import Calendar
from Model.reminder import Reminder
from Model.day import Day
from Model.month import Month
from Model.year import Year
from View.day_view import DayView
from View.calendar_view import CalendarView
import pickle

with open('cal.dat', 'rb') as f:
    cal = pickle.load(f)
c1 = Calendar()
day = Day(8)
m = Meeting('Interview', 2023, 8, 8, 'job interview', 3, 'Teams', '2:30')
r = Reminder('Make Dinner', 2023, 8, 8)
to = ToDo('Project', 2023, 8, 16, 'EECE2140 project')
day.add_task(m)
day.add_task(r)
day.add_task(to)

d = DayView(day)
d.schedule()
