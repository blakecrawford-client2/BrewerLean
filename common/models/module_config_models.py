from django.db import models


class BLModule (models.Model):
    class Meta:
        verbose_name_plural= 'BL1 Modules'
        verbose_name = 'BL1 Module'

    mod_code = models.CharField(max_length=5, default='X')
    mod_name = models.CharField(max_length=25,
                                 null=False,
                                 blank=False)
    mod_order = models.IntegerField(unique=True,
                                    null=True,
                                    blank=True)
    mod_enabled = models.BooleanField(default=True)
    mod_url_suffix = models.CharField(max_length=100,
                                      null=True,
                                      blank=True)

