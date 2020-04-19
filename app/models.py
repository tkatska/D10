from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    TRANSMISSION_TYPE = (
        (1, 'Mechanical'),
        (2, 'Automatic'),
        (3, 'Robotic'),
    )

    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(db_column='seriesYear', blank=True, null=True)
    transmission = models.SmallIntegerField(db_column='standardTransmission', choices=TRANSMISSION_TYPE)
    color = models.CharField(max_length=50, blank=True, null=True)

