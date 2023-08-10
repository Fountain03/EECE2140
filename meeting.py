from task import Task


class Meeting(Task):
    """This class represents a meeting task for a calendar"""

    def __init__(self, title: str, year, month, day,
                 desc: str, duration, location) -> None:
        """Creates a Meeting object

        Args:
            title (str): The title of the meeting
            year (int): Year of the meeting
            month (int): Month of the meeting
            day (int): Day of the meeting
            desc (str): Description of the meeting
            duration (int): how long the meeting is in hours
            location (str): where the meeting is
        """
        super().__init__(title, year, month, day)
        self.loc = location
        self.duration = duration
        self.desc = desc
