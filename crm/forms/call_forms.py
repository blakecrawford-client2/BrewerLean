from django import forms
from crm.models.crm_models import Call
from crm.models.crm_models import Tasting
from bootstrap_datepicker_plus.widgets import DatePickerInput

###########
# Call for to be used for debugging purposes, note that
# this call form is NOT USED in production, but rather
# the call wizard is used for all call generation and
# completion.
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


##########
# The call wizard works by creating a series of parameters
# inside a URL, so the real 'form' entry only cares about
# call notes and the dropped samples checkbox.  The view
# that handles this form takes care of taking the URL apart
# and trapping any errors
class CallWizardForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['note',
                  'samples']



class TastingForm(forms.ModelForm):
    tasting_date = forms.DateField(
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                "format": "DD MMM YYYY",
                "showClose": True,
                "showClear":True,
                "showTodayButton": True,
            }
        )
    )

    class Meta:
        model = Tasting
        fields = ['tasting_date',
                  'estimated_interations',
                  'estimated_attributable_units_sold',
                  'estimated_units_used',
                  'sentiment',
                  'notes']





