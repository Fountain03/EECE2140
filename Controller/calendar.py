import pickle
from View.calendar_view import CalendarView


class Controller:

    def __init__(self, cv) -> None:
        self.cv = cv
        cv.menu()
