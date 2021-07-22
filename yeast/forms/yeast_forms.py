from django import forms
from yeast.models.master_data_yeast import *

class LabForm(forms.ModelForm):
    class Meta:
        model = YeastLab
        fields = ['yeast_lab_code',
                  'yeast_lab_name']

