from django import forms

from product.models import ProductServiceInfo
from ebs.models.master_data_products import Product

class ProductServiceInfoForm(forms.ModelForm):
    class Meta:
        model = ProductServiceInfo
        fields = ('product',
                  'style_detail',
                  'label_abv',
                  'tap_regulator_psi',
                  'public_tasting_notes',
                  'may_also_like',
                  'picture',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('ownership',
                  'product_type',
                  'product_name',)