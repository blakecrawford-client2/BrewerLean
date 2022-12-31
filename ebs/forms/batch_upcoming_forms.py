from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from tempus_dominus.widgets import DatePicker
from ebs.models.brew_sheets import Batch
from ebs.models.master_data_facilities import Tank
from ebs.models.master_data_facilities import Staff
from ebs.models.master_data_products import Product


###
# form for creating a new 'upcoming' batch
class MakeUpcomingBatchForm(forms.ModelForm):
    plan_start_day = forms.DateField(
        input_formats=['%d %b %Y'],
        widget=DatePicker(
            options={
                'format': 'DD MMM YYYY',
                'useCurrent': True,
                'timeZone': 'EST',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_fv'].queryset = Tank.objects.filter(tank_type='FV').order_by('tank_name')
        self.fields['batch_product'].queryset = Product.objects.order_by('product_name')

    class Meta:
        model = Batch
        fields = ['batch_product', 'schedule_pattern', 'plan_start_day', 'target_fv']

###
# Form for 'starting' a batch that is in the
# 'upcoming' list
class StartUpcomingBatchForm(forms.ModelForm):
    brewer = forms.ModelChoiceField(queryset=Staff.objects.filter(is_active=True).order_by('name'))
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
        self.fields['target_fv'].queryset = Tank.objects.filter(tank_type='FV').order_by('tank_name')
        self.fields['target_bt'].queryset = Tank.objects.filter(tank_type='BT').order_by('tank_name')
        self.fields['batch_product'].disabled = True
        self.fields['schedule_pattern'].disabled = True
        self.fields['plan_start_day'].disabled = True

