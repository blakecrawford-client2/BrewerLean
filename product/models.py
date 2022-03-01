from django.db import models
from django.contrib.auth.models import User

from ebs.models.master_data_products import Product
from ebs.models.master_data_products import ProductType

# Create your models here.
class ProductServiceInfo(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
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