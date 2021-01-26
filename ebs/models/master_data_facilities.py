from django.db import models

class Facility(models.Model):
    facility_name = models.CharField(max_length=100)

class Tank(models.Model):
    class TankType(models.TextChoices):
        FERMENTER = 'FV', 'Fermenter'
        BRITE = 'BT', 'brite'

    tank_type = models.CharField(max_length=2,
                                 choices=TankType.choices,
                                 default=TankType.FERMENTER)
    tank_name = models.CharField(max_length=15)


