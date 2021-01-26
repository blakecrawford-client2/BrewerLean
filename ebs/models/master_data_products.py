from django.db import models
from ebs.models.master_data_partners import *

class ProductType(models.Model):
    product_type = models.CharField(max_length=10)

class Product(models.Model):
    ownership = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=100, null=False)