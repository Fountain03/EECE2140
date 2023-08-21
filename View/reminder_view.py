from Model.reminder import Reminder
from View.task_view import TaskView
import tkinter as tk
import datetime


class ReminderView(TaskView):
    """This class represents the GUI visualization for a reminder task
    """

    def __init__(self, task) -> None:
        """Creates a GUI visual for the given reminder

        Args:
            task (Task): the given reminder
        """
        super().__init__(task)

    def create(self, cal):
        """Allows user to create a reminder and add to calendar

        Args:
            cal (Calendar): the given calendar
        """
        # Provides what information is required for user to submit
        f1 = tk.Frame(self.disp)
        title_label = tk.Label(master=f1, text='Title')
        title_label.pack(side=tk.LEFT)
        title_entry = tk.Entry(master=f1)
        title_entry.pack(side=tk.RIGHT)

        f2 = tk.Frame(self.disp)
        date_label = tk.Label(master=f2, text='Date M/D/YYYY')
        date_label.pack(side=tk.LEFT)
        month_entry = tk.Entry(master=f2, width=2)
        day_entry = tk.Entry(master=f2, width=2)
        year_entry = tk.Entry(master=f2, width=4)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()
        f2.pack()

        def accept():
            """Compiles information and creates a new object
            """
            title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            self.task = Reminder(title, year, month, day)
            cal.add_task(self.task)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='save',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)

    def edit(self, button, cal):
        """Allows user to edit existing reminders in the calendar

        Args:
            button (Button): Visual with information of reminder to be updated
            cal (Calendar): the calendar the reminder belongs to
        """

        # displays current information and allows user to edit directly
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
        month_entry.insert(0, self.task.date.month)
        year_entry.insert(0, self.task.date.year)
        day_entry.insert(0, self.task.date.day)
        month_entry.pack(side=tk.LEFT)
        day_entry.pack(side=tk.LEFT)
        year_entry.pack(side=tk.LEFT)
        f1.pack()
        f2.pack()

        def accept():
            """Compiles user given information to edit reminder
            """
            self.task.title = title_entry.get()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())

            if self.task.date != datetime.date(year, month, day):
                self.task.date = datetime.date(year, month, day)
                cal.add_task(self.task)
                cal.update()
            self.task.date = datetime.date(year, month, day)
            button['text'] = str(self.task)
            self.disp.destroy()

        new_button = tk.Button(self.disp, text='save',
                               command=accept)
        new_button.pack(side=tk.BOTTOM)
