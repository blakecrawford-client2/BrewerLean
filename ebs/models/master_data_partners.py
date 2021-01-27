from django.db import models
from django.contrib.auth.models import User

class PartnerType(models.Model):
    partner_type = models.CharField(max_length=25)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Partner(models.Model):
    partner_name = models.CharField(max_length=100)
    partner_type = models.ForeignKey(PartnerType, null=True, on_delete=models.SET_NULL)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)