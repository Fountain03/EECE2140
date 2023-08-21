from Model.meeting import Meeting
from Model.todo import ToDo
from Model.planner import Calendar
from Model.reminder import Reminder
from View.calendar_view import CalendarView
from Model.date import Date
from View.daily_view import DailyView
from View.meeting_view import MeetingView
from View.daily_view import DailyView
import datetime
import tkinter as tk
import unittest


class TestTasks(unittest.TestCase):
    date = None
    m = None
    r = None
    t = None
    c = None

    def init():
        TestTasks.c = Calendar()
        TestTasks.date = Date(datetime.date(2023, 8, 20))
        TestTasks.m = Meeting('meeting', 2023, 8, 20, 'test',
                              2, 'teams', '2:30')
        TestTasks.r = Reminder('reminder', 2023, 8, 20)
        TestTasks.t = ToDo('todo', 2023, 8, 20, 'test')

    def test_meeting(self):
        TestTasks.init()
        self.assertEqual(TestTasks.m.full_time(), '4:30')
        self.assertEqual(str(TestTasks.m), 'meeting\ntest\n2:30-4:30\nteams\n')

    def test_reminder(self):
        TestTasks.init()
        self.assertEqual(str(TestTasks.r), 'reminder\n')

    def test_todo(self):
        TestTasks.init()
        self.assertEqual(
            str(TestTasks.t), 'todo\ntest')

    def test_date(self):
        TestTasks.init()
        self.assertNotIn(TestTasks.r, TestTasks.date.tasks)
        TestTasks.date.add_task(TestTasks.r)
        self.assertIn(TestTasks.r, TestTasks.date.tasks)
        self.assertEqual(str(TestTasks.date),
                         f'2023-08-20\n{str(TestTasks.r)}\n')
        TestTasks.date.remove_task(TestTasks.r)
        self.assertNotIn(TestTasks.r, TestTasks.date.tasks)
        self.assertEqual(str(TestTasks.date), '2023-08-20\nNo tasks today!')

    def test_date_update(self):
        TestTasks.init()
        TestTasks.date.add_task(TestTasks.r)
        self.assertIn(TestTasks.r, TestTasks.date.tasks)
        TestTasks.r.date = datetime.date(2023, 8, 22)
        TestTasks.date.update()
        self.assertNotIn(TestTasks.r, TestTasks.date.tasks)

    def test_calendar(self):
        TestTasks.init()
        self.assertNotIn(TestTasks.r.date, TestTasks.c.dates.values())
        TestTasks.c.add_task(TestTasks.r)
        self.assertIn(TestTasks.r.date, TestTasks.c.dates)
        self.assertEqual(TestTasks.c.today(),
                         Date(datetime.date.today()))
        TestTasks.r.date = datetime.date(2023, 8, 22)
        TestTasks.c.update()
        self.assertEqual(TestTasks.c.get_date(datetime.date(2023, 8, 20)),
                         Date(datetime.date(2023, 8, 20)))
