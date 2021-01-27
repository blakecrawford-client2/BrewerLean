from django.db import models
from django.contrib.auth.models import User

class Facility(models.Model):
    facility_name = models.CharField(max_length=100)

class Tank(models.Model):
    class TankType(models.TextChoices):
        FERMENTER = 'FV', 'Fermenter'
        BRITE = 'BT', 'Brite'
        UNI = 'UT', 'Unitank'

    tank_type = models.CharField(max_length=2,
                                 choices=TankType.choices,
                                 default=TankType.FERMENTER)
    tank_name = models.CharField(max_length=15)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


