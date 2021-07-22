from django.db import models
from django.contrib.auth.models import User

class YeastLab(models.Model):
    class Meta:
        verbose_name = 'Yeast Lab'
        verbose_name_plural = 'Yeast Labs'
    yeast_lab_code = models.CharField(max_length=4)
    yeast_lab_name = models.CharField(max_length=250)

    def __str__(self):
        return self.yeast_lab_name

    def __unicode__(self):
        return self.yeast_lab_name


class Yeast(models.Model):
    class Meta:
        verbose_name = 'Yeast'
        verbose_name_plural = 'Yeasts'

    class YeastFormat(models.TextChoices):
        LIQUID = 'L', 'Liquid'
        DRY = 'D', 'Dry'

    yeast_lab = models.ForeignKey(YeastLab,
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)
    yeast_name = models.CharField(max_length=250)
    yeast_format = models.CharField(max_length=1,
                                    choices=YeastFormat.choices,
                                    default=YeastFormat.DRY)
    is_nutrient_required = models.BooleanField(default=True)
    is_harvestable = models.BooleanField(default=True)


class Brink(models.Model):
    class Meta:
        verbose_name = 'Brink'
        verbose_name_plural = 'Brinks'

    class BrinkTypes(models.TextChoices):
        DRYBRICK = 'Dry Brick'
        LABPKG = 'Lab Packaging'
        KEG = 'Keg Brink'
        BUCKET = 'Bucket'

    brink_name = models.CharField(max_length=250)
    brink_capacity = models.CharField(max_length=250)


class YeastPitch(models.Model):
    class Meta:
        verbose_name = 'Yeast Pitch'
        verbose_name_plural = 'Yeast Pitches'

    lot_code = models.CharField(max_length=100,
                                null=True,
                                blank=True)
    generation = models.IntegerField(default=0)
    yeast = models.ForeignKey(Yeast,
                              null=True,
                              on_delete=models.SET_NULL)
    brink = models.ForeignKey(Brink,
                              null=True,
                              on_delete=models.SET_NULL)
    parent_pitch = models.ForeignKey('self',
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     default=None)


class CellCount(models.Model):
    class Meta:
        verbose_name = 'Cell Count'
        verbose_name_plural = 'Cell Counts'

    pitch = models.ForeignKey(YeastPitch,
                              null=True,
                              on_delete=models.SET_NULL,
                              default=None)
    count = models.DecimalField(max_digits=14,
                                decimal_places=4,
                                null=True)

    volume = models.DecimalField(max_digits=5,
                                 decimal_places=1,
                                 null=True)

