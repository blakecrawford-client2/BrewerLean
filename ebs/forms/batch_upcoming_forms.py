from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from tempus_dominus.widgets import DatePicker
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchPackagePlan
from ebs.models.master_data_facilities import Tank
from ebs.models.master_data_facilities import Staff
from ebs.models.master_data_products import Product



###
# form for creating a new 'upcoming' batch
class MakeUpcomingBatchForm(forms.ModelForm):
    plan_start_day = forms.DateField(
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YYYY',
                'useCurrent': True,
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_fv'].queryset = Tank.objects.filter(tank_type='FV').order_by('tank_name')
        self.fields['batch_product'].queryset = Product.objects.filter(ownership__partner_active=True, product_active=True).order_by('ownership__partner_name', 'product_name')

    class Meta:
        model = Batch
        fields = ['batch_product',
                  'schedule_pattern',
                  'plan_start_day',
                  'total_batch_size',
                  'target_fv']


class UpcomingBatchPkgPlanForm(forms.ModelForm):
    class Meta:
        model = BatchPackagePlan
        fields = ('kg_half_owned',
                  'kg_half_oneway',
                  'kg_half_client',
                  'kg_half_client_oneway',
                  'kg_sixth_owned',
                  'kg_sixth_oneway',
                  'kg_sixth_client',
                  'kg_sixth_client_oneway',
                  'cs_12oz',
                  'cs_16oz',
                  'cs_500ml',
                  'cs_750ml',
                  'package_note')


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

