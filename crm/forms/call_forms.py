from django import forms
from django.utils.safestring import mark_safe
from crm.models.crm_models import Account
from crm.models.crm_models import Call


class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        widgets = {
            'type': forms.RadioSelect(),
            'method': forms.RadioSelect(),
            'outcome': forms.RadioSelect(),
            'follow_up_delay': forms.RadioSelect(),
        }
        fields = ['account',
                  'schedule_week',
                  'type',
                  'method',
                  'samples',
                  'outcome',
                  'follow_up_required',
                  'follow_up_delay',
                  'note',]


class CallWizardForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['note',
                  'samples']





