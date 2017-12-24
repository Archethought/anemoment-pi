from django.db import models


# Create your models here.
class WindData(models.Model):
    speed = models.FloatField()
    direction = models.FloatField()
    north_south = models.FloatField()
    west_east = models.FloatField()
    up_down = models.FloatField()
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)