from django.db import models
from django.contrib.auth.models import User

###
# A Facility is a building where beer
# production takes place
class Facility(models.Model):
    class Meta:
        verbose_name='Facility'
        verbose_name_plural='Facilities'
    facility_name = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_name

###
# a tank is a vessel of a utility type
# in which beer resides for process purposes
class Tank(models.Model):
    class Meta:
        verbose_name_plural='Tanks'
    class TankType(models.TextChoices):
        FERMENTER = 'FV', 'Fermenter'
        BRITE = 'BT', 'Brite'
        UNI = 'UT', 'Unitank'

    tank_type = models.CharField(max_length=2,
                                 choices=TankType.choices,
                                 default=TankType.FERMENTER)
    tank_name = models.CharField(max_length=15)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.tank_name

###
# Staff are people with login privileges who also
# have a role.  This didn't workout as intended and
# can be considered deprecated for all intents and
# purposes.
class Staff(models.Model):
    class Meta:
        verbose_name_plural = 'Staff'

    class StaffRole(models.TextChoices):
        HOTSIDE = 'HS', 'Hot Side'
        COLDSIDE = 'CS', 'Cold Side'
        WAREHOUSE = 'WS', 'Warehouse'

    name = models.CharField(max_length=75, null=True)
    role = models.CharField(max_length=2,
                            choices=StaffRole.choices,
                            default=StaffRole.HOTSIDE)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.name

