from django.db import models
from datetime import datetime, timedelta


class WindData(models.Model):
    speed = models.FloatField()
    direction = models.FloatField()
    north_south = models.FloatField()
    west_east = models.FloatField()
    up_down = models.FloatField()
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_published_within(self, start_time, end_time=datetime.now()):
        """
        Determine if the timestamp value falls between start and end time.
        :type start_time: datetime
        :param end_time:  Not required -- defaults to now
        :type end_time: datetime
        :return: True or False
        """
        return start_time <= self.timestamp <= end_time


class RawInputError(models.Model):
    E_INVALID = 0
    E_INCOMPLETE = 1

    ERROR_TYPES = (
        (E_INVALID, "Invalid Data"),
        (E_INCOMPLETE, "Incomplete Data"),
    )

    type = models.CharField(max_length=1, choices=ERROR_TYPES)
    raw_input = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


