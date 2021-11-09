from django.db import models
from django.contrib.auth.models import User

###
# a Partner Type defines the relationship
# between a client and the production facility.
# really only useful for contract brewing... if you
# only make your own brands, you'll still need on
# type and one partner.
class PartnerType(models.Model):
    class Meta:
        verbose_name_plural = 'Partner Types'

    partner_type = models.CharField(max_length=25)

    def __str__(self):
        return self.partner_type

###
# The name of a company for whom beer is produced.
class Partner(models.Model):
    class Meta:
        verbose_name_plural = 'Partners'

    partner_name = models.CharField(max_length=100)
    partner_short_code = models.CharField(max_length=4, null=True)
    partner_type = models.ForeignKey(PartnerType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.partner_name