from django.db import models

class Originator(models.Model):
    class Meta:
        verbose_name_plural='Originators'
    originator_name = models.CharField(max_length=100)

    def __str__(self):
        return self.originator_name

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
    material_origin = models.ForeignKey(Originator, null=True, on_delete=models.SET_NULL)
    material_name = models.CharField(max_length=100)

    def __str__(self):
        return self.material_name