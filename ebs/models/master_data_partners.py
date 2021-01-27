from django.db import models
from django.contrib.auth.models import User

class PartnerType(models.Model):
    class Meta:
        verbose_name_plural = 'Partner Types'

    partner_type = models.CharField(max_length=25)

    def __str__(self):
        return self.partner_type

class Partner(models.Model):
    class Meta:
        verbose_name_plural = 'Partners'

    partner_name = models.CharField(max_length=100)
    partner_type = models.ForeignKey(PartnerType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.partner_name