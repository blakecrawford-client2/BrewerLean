from django.db import models
from ebs.models.master_data_partners import *

###
# Products are the things that are manufactured... individual
# beers.  Product Types are intented to be things like "ale"
# or "lager" but can really be anything you find useful.
class ProductType(models.Model):
    class Meta:
        verbose_name_plural='Product Types'

    product_type = models.CharField(max_length=10)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.product_type

###
# A product is a thing that is being manufactured, and they
# are of a type and have an ownership.
class Product(models.Model):
    class Meta:
        verbose_name_plural='Products'
        ordering=['product_name']

    ownership = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=100, null=False)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.product_name
