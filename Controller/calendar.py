import pickle
from View.calendar_view import CalendarView


class Controller:

    def __init__(self, cv) -> None:

        with open(cv, 'rb') as f:
            cal = pickle.load(f)
        self.cv = CalendarView(cal)
        self.cv.menu()
