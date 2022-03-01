from django import forms

from product.models import ProductServiceInfo

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