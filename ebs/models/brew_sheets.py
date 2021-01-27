from django.db import models
from django.contrib.auth.models import User

from ebs.models.master_data_products import Product
from ebs.models.master_data_facilities import Tank, Staff
from ebs.models.master_data_rawmaterials import Material

class SchedulePattern(models.Model):
    class Meta:
        verbose_name_plural = 'Schedule Patterns'

    pattern_name = models.CharField(max_length=25)
    pattern_total_days = models.IntegerField(null=True)
    offset_yeast_crash = models.IntegerField(null=True)
    offset_yeast_harvest = models.IntegerField(null=True)
    offset_dryhop = models.IntegerField(null=True)
    offset_final_crash = models.IntegerField(null=True)
    offset_transfer = models.IntegerField(null=True)
    offset_package = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.pattern_name

class BatchSize(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Sizes'

    batch_size_name = models.CharField(max_length=25)

    def __str__(self):
        return self.batch_size_name

class Batch(models.Model):
    class Meta:
        verbose_name_plural = 'Batches'

    batch_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    brewer = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    total_batch_size = models.ForeignKey(BatchSize, null=True, on_delete=models.SET_NULL)
    schedule_pattern = models.ForeignKey(SchedulePattern, null=True, on_delete=models.SET_NULL)
    qty_turns = models.IntegerField(null=True)
    qty_brew_days = models.IntegerField(null=True)
    is_dh = models.BooleanField()
    qty_dh_days = models.IntegerField(null=True)
    target_fv = models.ForeignKey(Tank, null=True, on_delete=models.SET_NULL, related_name='+')
    target_bt = models.ForeignKey(Tank, null=True, on_delete=models.SET_NULL, related_name='+')
    obeer_batch = models.IntegerField(null=True)
    obeer_mpn = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.batch_product.ownership.partner_name + '::' + self.batch_product

class BatchPlanDates(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Plan Dates'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    brew_date = models.DateField(null=True)
    yeast_crash_date = models.DateField(null=True)
    yeast_harvest_date = models.DateField(null=True)
    dryhop_date = models.DateField(null=True)
    final_crash_date = models.DateField(null=True)
    transfer_date = models.DateField(null=True)
    package_date = models.DateField(null=True)

    def __str__(self):
        return self.brew_date

class BatchActualDates(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Actual Dates'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    brew_date = models.DateField(null=True)
    yeast_crash_date = models.DateField(null=True)
    yeast_harvest_date = models.DateField(null=True)
    dryhop_date = models.DateField(null=True)
    final_crash_date = models.DateField(null=True)
    transfer_date = models.DateField(null=True)
    package_date = models.DateField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.brew_date

class BatchRawMaterialsLog(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Raw Materials Logs'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    material_qty = models.CharField(max_length=25, null=True)
    material_lot = models.CharField(max_length=100, null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.material.material_name

class BatchWortQC(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Wort QC Data'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    brewer = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    turn = models.IntegerField(null=False)
    temp_mash = models.DecimalField(max_digits=4, decimal_places=1)
    ph_mash = models.DecimalField(max_digits=2, decimal_places=1)
    volume_strike = models.DecimalField(max_digits=3, decimal_places=0)
    volume_sparge = models.DecimalField(max_digits=3, decimal_places=0)
    volume_postboil = models.DecimalField(max_digits=3, decimal_places=0)
    extract_first_runnings = models.DecimalField(max_digits=3, decimal_places=1)
    extract_preboil = models.DecimalField(max_digits=3, decimal_places=1)
    extract_postboil = models.DecimalField(max_digits=3, decimal_places=1)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.turn

class BatchYeastPitch(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Yeast Pitches'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    yeast = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    yeast_qty = models.DecimalField(max_digits=4, null=True, decimal_places=1)
    yeast_source = models.CharField(max_length=100, null=True)
    yeast_pitch_temp = models.DecimalField(max_digits=3, null=True, decimal_places=1)
    yeast_pitch_turn = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.yeast.material_name

class BatchFermentationQC(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Fermentation QC Data'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    extract_apparent = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    sg_real_calculated = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    ph = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    temp_sv = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    temp_pv = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    extract_real = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.date

class BatchDOEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Batch DO Entries'

    class DOType(models.TextChoices):
        PREFERM = 'PE', 'Pre-Fermentation'
        POSTFERM = 'PT', 'Post-Fermentation'
        POSTDRYHOP = 'PD', 'Post Dry-Hop'
        ENDOFFERM = 'PF', 'Post-Fermentation'
        TRANSFER = 'TR', 'Transfer'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    do_type = models.CharField(max_length=2, choices=DOType.choices, default=DOType.PREFERM)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.do_type

class BatchTransfer(models.Model):
    class Meta:
        verbose_name_plural = 'Batch Transfers'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    volume_transfer_approx = models.DecimalField(max_digits=4, decimal_places=1)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.batch.batch_product.ownership + '::' + self.batch.batch_product.product_name


class PackagingRun(models.Model):
    class Meta:
        verbose_name_plural = 'Packaging Runs'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    carb_vols = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    filled_halfs = models.IntegerField(null=True)
    filled_sixtels = models.IntegerField(null=True)
    skids_kegs = models.IntegerField(null=True)
    filled_cases = models.IntegerField(null=True)
    skids_cases = models.IntegerField(null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.batch.batch_product.ownership + "::" + self.batch.batch_product.product_name

class CanningQC(models.Model):
    class Meta:
        verbose_name_plural = 'Canning QC Data'

    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    weight_can = models.IntegerField(null=True)
    measure_seam_height = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    measure_seam_width = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    measure_body_hook = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    measure_cover_hook = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    do_can = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.batch.batch_product.ownership + "::" + self.batch.batch_product.product_name
