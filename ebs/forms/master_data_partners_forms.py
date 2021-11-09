from django import forms
from ebs.models.master_data_partners import PartnerType

###
# NOTE:  partner data is partially implemented at the
# moment, with a preference for doing this in Django
# admin.
class PartnerTypeForm(forms.ModelForm):
    class Meta:
        model = PartnerType
        fields = ['partner_type']
