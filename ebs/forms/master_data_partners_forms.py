from django import forms
from ebs.models.master_data_partners import PartnerType

class PartnerTypeForm(forms.ModelForm):
    class Meta:
        model = PartnerType
        fields = ['partner_type']
