from django.db import models
from django.contrib.auth.models import User

from master_data_products import Product
from master_data_facilities import Tank
from master_data_rawmaterials import Material

class SchedulePattern(models.Model):
    pattern_name = models.CharField(max_length=25)
    pattern_total_days = models.IntegerField(null=True)
    offset_yeast_crash = models.IntegerField(null=True)
    offset_yeast_harvest = models.IntegerField(null=True)
    offset_dryhop = models.IntegerField(null=True)
    offset_final_crash = models.IntegerField(null=True)
    offset_transfer = models.IntegerField(null=True)
    offset_package = models.IntegerField(null=True)

class BatchSize(models.Model):
    batch_size_name = models.CharField(max_length=25, on_delete=models.SET_NULL)

class Batch(models.Model):
    batch_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    brewer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    total_batch_size = models.ForeignKey(BatchSize, null=True)
    schedule_pattern = models.ForeignKey(SchedulePattern, null=True)
    qty_turns = models.IntegerField(null=True)
    qty_brew_days = models.IntegerField(null=True)
    is_dh = models.BooleanField()
    qty_dh_days = models.IntegerField(null=True)
    target_fv = models.ForeignKey(Tank, null=True, on_delete=models.SET_NULL)
    target_bt = models.ForeignKey(Tank, null=True, on_delete=models.SET_NULL)
    obeer_batch = models.IntegerField(null=True)
    obeer_mpn = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class BatchPlanDates(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    brew_date = models.DateField(null=True)
    yeast_crash_date = models.DateField(null=True)
    yeast_harvest_date = models.DateField(null=True)
    dryhop_date = models.DateField(null=True)
    final_crash_date = models.DateField(null=True)
    transfer_date = models.DateField(null=True)
    package_date = models.DateField(null=True)

class BatchActualDates(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    brew_date = models.DateField(null=True)
    yeast_crash_date = models.DateField(null=True)
    yeast_harvest_date = models.DateField(null=True)
    dryhop_date = models.DateField(null=True)
    final_crash_date = models.DateField(null=True)
    transfer_date = models.DateField(null=True)
    package_date = models.DateField(null=True)

class BatchRawMaterialsLog(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    material_qty = models.CharField(max_length=25, null=True)
    material_lot = models.CharField(max_length=100, null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class BatchWortQC(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    turn = models.IntegerField(null=False)
    temp_mash = models.DecimalField(max_digits=4, decimal_places=1)
    ph_mash = models.DecimalField(max_digits=2, decimal_places=1)
    volume_strike = models.DecimalField(max_digits=3)
    volume_sparge = models.DecimalField(max_digits=3)
    volume_postboil = models.DecimalField(max_digits=3)
    extract_first_runnings = models.DecimalField(max_digits=3, decimal_places=1)
    extract_preboil = models.DecimalField(max_digits=3, decimal_places=1)
    extract_postboil = models.DecimalField(max_digits=3, decimal_places=1)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class BatchYeastPitch(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    yeast = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    yeast_qty = models.DecimalField(max_digits=4, null=True)
    yeast_source = models.CharField(max_length=100, null=True)
    yeast_pitch_temp = models.DecimalField(max_digits=3, null=True)
    yeast_pitch_turn = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class BatchFermentationQC(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    date = models.DateField(null=True)
    extract_apparent = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    sg_real_calculated = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    ph = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    temp_sv = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    temp_pv = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    extract_real = models.DecimalField(max_digits=3, decimal_places=1, null=True)

class BatchDOEntry(models.Model):
    class DOType(models.TextChoices):
        PREFERM = 'PE', 'Pre-Fermentation'
        POSTFERM = 'PT', 'Post-Fermentation'
        POSTDRYHOP = 'PD', 'Post Dry-Hop'
        ENDOFFERM = 'PF', 'Post-Fermentation'
        TRANSFER = 'TR', 'Transfer'

    batch = models.ForeignKey(Batch, null=False)
    do_type = models.CharField(max_length=2, choices=DOType.choices, default=DOType.PREFERM)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class BatchTransfer(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    volume_transfer_approx = models.DecimalField(max_digits=4, decimal_places=1)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class PackagingRun(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    carb_vols = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    filled_halfs = models.IntegerField(null=True)
    filled_sixtels = models.IntegerField(null=True)
    skids_kegs = models.IntegerField(null=True)
    filled_cases = models.IntegerField(null=True)
    skids_cases = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class CanningQC(models.Model):
    batch = models.ForeignKey(Batch, null=False)
    weight_can = models.IntegerField(max_length=3, null=True)
    measure_seam_height = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    measure_seam_width = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    measure_body_hook = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    measure_cover_hook = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    do_can = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
