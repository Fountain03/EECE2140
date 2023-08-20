import pickle
from View.calendar_view import CalendarView
from Model.planner import Calendar


class Controller:
    """This class represents the calendar controller"""

    def __init__(self) -> None:
        """Creates a Controller object"""

        # Ask user for load file/save file
        self.dat = input('Enter your calendar file(.dat) or NEW: ')

        if self.dat == 'NEW':
            self.dat = input('Enter file to save data to (.dat): ')
            self.cal = Calendar()
        else:
            with open(self.dat, 'rb') as f:
                self.cal = pickle.load(f)
        self.cv = CalendarView(self.cal, self.dat)
        self.cv.menu()
