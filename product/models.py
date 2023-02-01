from django.db import models
from django.contrib.auth.models import User

from ebs.models.master_data_products import Product
from ebs.models.master_data_products import ProductType

from ebs.models.master_data_rawmaterials import Material


class ProductMaterialsAbstract(models.Model):

    class MaterialPhase(models.TextChoices):
        MASH = 'MSH', 'Mash'
        HOTSIDE = 'HSD', 'Hotside'
        COLDSIDE = 'CSD', 'Coldside'

    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    material = models.ForeignKey(Material,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    material_qty = models.CharField(max_length=25,
                                    null=True,
                                    verbose_name='Quantity')
    material_phase = models.CharField(max_length=3,
                                      choices=MaterialPhase.choices,
                                      default=MaterialPhase.MASH)


class ProductSpecificationsInfo(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                limit_choices_to={'ownership_id': 1},
                                related_name='specs_info')
    product_abv = models.DecimalField(max_digits=3,
                                      decimal_places=1,
                                      default=5.5,
                                      null=True,
                                      blank=True)
    product_srm = models.IntegerField(default=5,
                                      null=True,
                                      blank=True)
    product_turbidity = models.IntegerField(null=True,
                                            blank=True)


class ProductOperationsInfo(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                limit_choices_to={'ownership_id': 1},
                                related_name='ops_info',
                                verbose_name='Operations Infos')
    default_package_yield = models.DecimalField(max_digits = 3,
                                                decimal_places=1,
                                                default=80.0)


class ProductServiceInfo(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                limit_choices_to={'ownership_id': 1},
                                related_name='service_info',
                                verbose_name='Product')
    style_detail = models.CharField(max_length=256,
                                    blank=True,
                                    null=True)
    label_abv = models.DecimalField(max_digits=3,
                                    decimal_places=1,
                                    null=True,
                                    blank=True,
                                    default=0.0)
    tap_regulator_psi = models.DecimalField(max_digits=3,
                                            decimal_places=1,
                                            null=True,
                                            blank=True,
                                            default=0.0)
    public_tasting_notes = models.TextField(null=True,
                                            blank=True,
                                            max_length=1000)
    may_also_like = models.TextField(null=True,
                                     blank=True,
                                     max_length=1000)
    picture = models.ImageField(upload_to='svc/%Y/%m/%d/',
                                blank=True,
                                null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)