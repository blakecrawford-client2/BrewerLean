from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from ebs.models.brew_sheets import Batch
from ebs.models.master_data_facilities import Tank

class MakeUpcomingBatchForm(forms.ModelForm):
    plan_start_day = forms.DateField(
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            attrs={'readonly':'readonly'},
            options={
                "ignoreReadonly": True,
                "format":"DD MMM YYYY",
                "showClose":True,
                "showClear":True,
                "showTodayButton":True,
            }
        )
    )
    class Meta:
        model = Batch
        fields = ['batch_product', 'schedule_pattern', 'plan_start_day', 'target_fv']

class StartUpcomingBatchForm(forms.ModelForm):
    class Meta:
        model=Batch
        fields = [
                  'batch_product',
                  'schedule_pattern',
                  'plan_start_day',
                  'brewer',
                  'total_batch_size',
                  'qty_turns',
                  'qty_brew_days',
                  'target_fv',
                  'target_bt',
                  ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['status'].initial = 'IP'
        #self.fields['status'].disabled = True
        self.fields['target_fv'].queryset = Tank.objects.filter(tank_type='FV').order_by('tank_name')
        self.fields['target_bt'].queryset = Tank.objects.filter(tank_type='BT').order_by('tank_name')
        self.fields['batch_product'].disabled = True
        self.fields['schedule_pattern'].disabled = True
        self.fields['plan_start_day'].disabled = True

