from Controller.calendar import Controller
from View.calendar_view import CalendarView
from Model.planner import Calendar
import pickle


with open('cal.dat', 'rb') as f:
    cal = pickle.load(f)

cv = CalendarView(cal)

c = Controller(cv)
