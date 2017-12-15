from django.db import models

# Create your models here.
class WindData(models.Model):
    X_AXIS = "X"
    Y_AXIS = "Y"
    Z_AXIS = "Z"
    AXIS_CHOICES = (
        (X_AXIS, "X-Axis"),
        (Y_AXIS, "Y-Axis"),
        (Z_AXIS, "Z-Axis"),
    )
    axis = models.CharField(max_length=2, choices=AXIS_CHOICES)
    speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)