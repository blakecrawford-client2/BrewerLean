from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from tempus_dominus.widgets import DatePicker
from ebs.models.master_data_facilities import Tank
from ebs.models.master_data_rawmaterials import Material
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchRawMaterialsLog
from ebs.models.brew_sheets import BatchWortQC
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchFermentationQC
from ebs.models.brew_sheets import BatchDOEntry
from ebs.models.brew_sheets import BatchTransfer
from ebs.models.brew_sheets import CarbonationQCEntry
from ebs.models.brew_sheets import PackagingRun
from ebs.models.brew_sheets import CanningQC
from ebs.models.brew_sheets import BatchNote
from ebs.models.brew_sheets import BatchPackagePlan


##########
# Convenience formn for updating the target FV
# of an in-process batch after it has been set
# in the start batch process.
class ChangeFVForm(forms.ModelForm):
    target_fv = forms.ModelChoiceField(queryset=Tank.objects.filter(tank_type='FV').order_by('tank_name'))

    class Meta:
        model = Batch
        fields = ['target_fv']

##########
# Convenience form for adding OBeer MPN and
# Batch number information.  Truly, this is silly
# to use OBeer-specific terminology.  Future work
# should generalized this to allow the use of
# BL-specific batch generation.
class AddObeerDataForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['obeer_batch',
                  'obeer_mpn', ]

###
# Detail form for adding raw material records to a
# material log
class AddRawMaterialsForm(forms.ModelForm):
    material = forms.ModelChoiceField(queryset=Material.objects.filter(material_active=True).order_by('material_type', 'material_name'))
    class Meta:
        model = BatchRawMaterialsLog
        fields = ['material',
                  'material_lot',
                  'material_qty',
                  'is_dh',]

###
# Detail form for adding wort QC info
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


###
# Detail form for adding yeast pitch info
class AddYeastPitchEntryForm(forms.ModelForm):
    yeast = forms.ModelChoiceField(queryset=Material.objects.filter(material_type='YT'))
    class Meta:
        model = BatchYeastPitch
        fields = [
            'yeast',
            'yeast_qty',
            'yeast_source',
            'yeast_pitch_temp',
            'yeast_pitch_turn'
        ]


###
# Detail form for adding/changing actual dates, but
# note that this is counter-balanced by new  features
# that automatically populate the actual dates based on
# other details, such as DH, etc.  The need to edit
# actual dates is somewhat obviated by this, but we're
# leaving it in for now.
class UpdateActualDatesForm(forms.ModelForm):
    brew_date = forms.DateField(
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    yeast_crash_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    yeast_harvest_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    dryhop_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    final_crash_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    transfer_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    package_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

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

###
# Detail form for adding ferm QC data
class BatchFermentationQCForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

    class Meta:
        model = BatchFermentationQC
        fields = [
            'date',
            'extract_real',
            'ph',
            'temp_sv',
            'temp_pv'
        ]

###
# Detail form for adding a DO measurement
class BatchDOEntryForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

    class Meta:
        model = BatchDOEntry
        fields = [
                  'date',
                  'do_type',
                  'do_measurement']

###
# Detail form for adding FV->BT transfer
# information.
class BatchTransferForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['to_tank'].queryset = Tank.objects.filter(tank_type='BT').order_by('tank_name')

    class Meta:
        model = BatchTransfer
        fields = [
                  'date',
                  'volume_transfer_approx',
                  'to_tank']

###
# Detail form for adding carb info
class CarbonationQCEntryForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

    class Meta:
        model = CarbonationQCEntry
        fields = [
                  'date',
                  'carb_vols_brite']

###
# Detail form for adding Packaging info
class PackagingRunForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

    class Meta:
        model = PackagingRun
        fields = [
                  'date',
                  'filled_halfs',
                  'filled_sixtels',
                  'skids_kegs',
                  'filled_cases',
                  'skids_cases',
                  'line_count']

###
# Detail form for adding canning qc info
# like weights, seams, etc.
class CanningQCForm(forms.ModelForm):
    date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )

    class Meta:
        model = CanningQC
        fields = [
                  'date',
                  'type',
                  'measurement']

###
# Detail form for batch notes
class BatchNoteForm(forms.ModelForm):

    class Meta:
        model = BatchNote
        fields = ['note_type',
                  'note']

###
# New Feature in V0.7, the "harvest" function
# is built out to include the disposition of
# the yeast.
class YeastCrashHarvestForm(forms.Form):
    OPTIONS = [('1','Dry Pitch Discarded'),
               ('2','Dry Pitch Harvested'),
               ('3','Wet Pitch Discarded'),
               ('4','Wet Pitch Harvested')]
    yeast_crash_date = forms.DateField(label='Yeast Crash Date',
                                       required=False,
                                       #input_formats=['%d %b %Y'],
                                       widget=DatePickerInput(
                                           options={
                                               'format': 'DD MMM YY',
                                               'useCurrent': True,
                                           }
                                       ))
    yeast_harvest_date = forms.DateField(label='Yeast Harvest Date',
                                       required=False,
                                       #input_formats=['%d %b %Y'],
                                         widget=DatePickerInput(
                                             options={
                                                 'format': 'DD MMM YY',
                                                 'useCurrent': True,
                                             }
                                         ))

###
# Detail form for tracking the final crash
# date (this is prior to FV->BT transfer in
# most processes
class FinalCrashForm(forms.ModelForm):
    final_crash_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    class Meta:
        model = BatchActualDates
        fields = ['final_crash_date']


class DryHopForm(forms.ModelForm):
    dryhop_date = forms.DateField(
        required=False,
        #input_formats=['%d %b %Y'],
        widget=DatePickerInput(
            options={
                'format': 'DD MMM YY',
                'useCurrent': True,
            }
        )
    )
    class Meta:
        model = BatchActualDates
        fields = ['dryhop_date']


class InProcessBatchPkgPlanForm(forms.ModelForm):
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