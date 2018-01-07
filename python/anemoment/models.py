from django.db import models
from django.utils import timezone

class WindData(models.Model):
    wind_speed_3d = models.FloatField()
    horizontal_wind_direction = models.FloatField()
    u_vector = models.FloatField()
    v_vector = models.FloatField()
    w_vector = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    compass_heading = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def is_published_within(self, start_time, end_time=timezone.now()):
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


