from Model.task import Task


class Meeting(Task):
    """This class represents a meeting task for a calendar"""

    def __init__(self, title: str, year, month, day,
                 desc: str, duration, location, time) -> None:
        """Creates a Meeting object

        Args:
            title (str): The title of the meeting
            year (int): Year of the meeting
            month (int): Month of the meeting
            day (int): Day of the meeting
            desc (str): Description of the meeting
            duration (int): how long the meeting is in hours
            location (str): where the meeting is
            time(str): the time the meeting starts
        """
        super().__init__(title, year, month, day)
        self.loc = location
        self.duration = duration
        self.desc = desc
        self.start = time

    def full_time(self):
        length = self.duration * 60
        hour, min = self.start.split(':')
        hour = int(hour)
        min = int(min)
        min += length
        while min >= 60:
            min -= 60
            hour += 1
        return f'{hour}:{min: 03d}'

    def __str__(self) -> str:
        return super().__str__() +\
            f'{self.desc}\n'\
            f'{self.start}-{self.full_time()}\n'\
            f'{self.loc}\n'
