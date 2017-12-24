from django.db import models


class WindData(models.Model):
    speed = models.FloatField()
    direction = models.FloatField()
    north_south = models.FloatField()
    west_east = models.FloatField()
    up_down = models.FloatField()
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


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


