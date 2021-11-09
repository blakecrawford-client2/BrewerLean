from django.db import models
from django.contrib import admin

###
# An originator is a brand of raw materials.  "Simpson's"
# or "Weyermann" for example.  It's not intended to be a
# distributor such as BSG or CMG, but there's no reason
# why it couldn't be.
class Originator(models.Model):
    class Meta:
        verbose_name_plural='Originators'
    originator_name = models.CharField(max_length=100)

    def __str__(self):
        return self.originator_name

###
# A material is an ingredient, more or less.  The
# granularity with which you want to manage materials is
# entirely up to you.
#TODO: Raw materials management needs significant fleshing out
#TODO:  Yeast management needs significant fleshing out
class Material(models.Model):
    class Meta:
        verbose_name_plural='Materials'

    class MaterialType(models.TextChoices):
        GRAIN = 'GR', 'Grain'
        HOPS = 'HP', 'Hops'
        YEAST = 'YT', 'Yeast'
        OTHER = 'OT', 'Other'

    material_type = models.CharField(max_length=2, choices=MaterialType.choices, default=MaterialType.GRAIN)
    material_origin = models.ForeignKey(Originator, null=True, blank=True, on_delete=models.SET_NULL)
    material_name = models.CharField(max_length=100)
    material_obeer_code = models.CharField(max_length=25, null=True, blank=True)
    material_test_field = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        #return self.material_type + '::' + self.material_origin.originator_name + '::' + self.material_name
        return self.material_type + '::' + self.material_name