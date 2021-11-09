from django import forms
from ebs.models.brew_sheets import Batch

##########
# Just for changing the status of a batch to 'archived'
class CloseBatchForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Batch.BatchStatus.choices, initial=Batch.BatchStatus.choices[2])

    class Meta:
        model = Batch
        fields = ['status']