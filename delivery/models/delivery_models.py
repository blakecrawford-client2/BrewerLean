from django.db import models
from django.contrib.auth.models import User

class DeliveryMetrics(models.Model):
    class Meta:
        verbose_name_plural = 'Delivery Metrics'

    delivery_date = models.DateField(null=True,
                                     blank=True)
    cases_out = models.IntegerField(null=True,
                                    blank=True)
    halfs_out = models.IntegerField(null=True,
                                    blank=True)
    sixtels_out = models.IntegerField(null=True,
                                      blank=True)
    halfs_in = models.IntegerField(null=True,
                                   blank=True)
    sixtels_in = models.IntegerField(null=True,
                                     blank=True)
    time_out = models.TimeField(null=True,
                                blank=True)
    time_in = models.TimeField(null=True,
                               blank=True)
    miles_start = models.IntegerField(null=True,
                                      blank=True)
    miles_end = models.IntegerField(null=True,
                                    blank=True)
    total_stops= models.IntegerField(null=True,
                                     blank=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)