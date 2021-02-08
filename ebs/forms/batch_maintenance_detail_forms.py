from django import forms
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchRawMaterialsLog

class AddObeerDataForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['obeer_batch',
                  'obeer_mpn',]

class AddRawMaterialsForm(forms.ModelForm):
    class Meta:
        model = BatchRawMaterialsLog
        fields = ['material',
                  'material_lot',
                  'material_qty']