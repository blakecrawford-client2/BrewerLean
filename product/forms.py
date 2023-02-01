from django import forms

from product.models import ProductServiceInfo
from product.models import ProductOperationsInfo
from product.models import ProductMaterialsAbstract
from ebs.models.master_data_products import Product

class ProductServiceInfoForm(forms.ModelForm):
    class Meta:
        model = ProductServiceInfo
        fields = (
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
                  'product_name',
                  'product_active')


class ProductOpsInfoForm(forms.ModelForm):
    class Meta:
        model = ProductOperationsInfo
        fields = ('default_package_yield',)


class ProductMaterialsAbstractItemForm(forms.ModelForm):
    class Meta:
        model = ProductMaterialsAbstract
        fields = ('material',
                  'material_qty',
                  'material_phase')