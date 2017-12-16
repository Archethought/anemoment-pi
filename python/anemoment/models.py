from django.db import models

# Create your models here.
class WindData(models.Model):
    x_speed = models.FloatField()
    y_speed = models.FloatField()
    z_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)