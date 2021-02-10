from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchRawMaterialsLog
from ebs.models.brew_sheets import BatchWortQC
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchFermentationQC

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

class AddWortQCEntryForm(forms.ModelForm):
    class Meta:
        model = BatchWortQC
        fields = [
            'brewer',
            'turn',
            'temp_mash',
            'ph_mash',
            'volume_strike',
            'volume_sparge',
            'extract_first_runnings',
            'extract_last_runnings',
            'volume_preboil',
            'extract_preboil',
            'volume_postboil',
            'extract_postboil',
        ]

class AddYeastPitchEntryForm(forms.ModelForm):
    class Meta:
        model = BatchYeastPitch
        fields = [
            'staff',
            'yeast',
            'yeast_qty',
            'yeast_source',
            'yeast_pitch_temp',
            'yeast_pitch_turn'
        ]

class UpdateActualDatesForm(forms.ModelForm):
    brew_date = forms.DateField(
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    yeast_crash_date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    yeast_harvest_date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    dryhop_date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    final_crash_date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    transfer_date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    package_date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    class Meta:
        model = BatchActualDates
        fields = [
            'brew_date',
            'yeast_crash_date',
            'yeast_harvest_date',
            'dryhop_date',
            'final_crash_date',
            'transfer_date',
            'package_date',
        ]


class BatchFermentationQCForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
            "format":"DD MMM YYYY",
            "showClose":True,
            "showClear":True,
            "showTodayButton":True,}))
    class Meta:
        model = BatchFermentationQC
        fields = [
            'staff',
            'date',
            'extract_apparent',
            'extract_real',
            'sg_real_calculated',
            'temp_sv',
            'temp_pv'
        ]