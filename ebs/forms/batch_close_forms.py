from django import forms
from ebs.models.brew_sheets import Batch


class CloseBatchForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Batch.BatchStatus.choices, initial=Batch.BatchStatus.choices[2])
    class Meta:
        model = Batch
        fields = ['status']