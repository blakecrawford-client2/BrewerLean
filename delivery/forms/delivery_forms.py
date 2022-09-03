from django import forms
from django.utils.safestring import mark_safe
from delivery.models.delivery_models import DeliveryMetrics
from bootstrap_datepicker_plus.widgets import DatePickerInput
from tempus_dominus.widgets import DatePicker


class DeliveryForm(forms.ModelForm):
    delivery_date = forms.DateField(
        input_formats=['%d %b %Y'],
        widget=DatePicker(
            options={
                'format': 'DD MMM YYYY',
                'useCurrent': True,
            }
        )
    )
    # delivery_date = forms.DateField(
    #     input_formats=['%d %b %Y'],
    #     widget=DatePickerInput(
    #         options={
    #             "format": "DD MMM YYYY",
    #             "showClose": True,
    #             "showClear": True,
    #             "showTodayButton": True,
    #         }
    #     )
    # )
    class Meta:
        model = DeliveryMetrics
        fields = ['delivery_date',
                  'total_stops',
                  'cases_out',
                  'halfs_out',
                  'sixtels_out',
                  'time_out',
                  'miles_start',
                  'miles_end',
                  'time_in',
                  'halfs_in',
                  'sixtels_in']