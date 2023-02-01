from django.contrib import admin
from django.apps import apps
from ebs.models.master_data_products import *
from ebs.models.master_data_partners import *
from ebs.models.master_data_facilities import *
from ebs.models.master_data_rawmaterials import *
from ebs.models.brew_sheets import *
# Special Registrations here

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(PartnerType)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('partner_name', 'partner_type', 'partner_active')
    ordering = ('partner_name', 'partner_active')

admin.site.register(Facility)
admin.site.register(Tank)
admin.site.register(Originator)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'material_type', 'material_origin', 'material_active')

admin.site.register(SchedulePattern)
admin.site.register(BatchSize)
admin.site.register(Batch)
admin.site.register(BatchPlanDates)
admin.site.register(BatchActualDates)
admin.site.register(BatchRawMaterialsLog)
admin.site.register(BatchWortQC)
admin.site.register(BatchYeastPitch)
admin.site.register(BatchFermentationQC)
admin.site.register(BatchDOEntry)
admin.site.register(BatchTransfer)
admin.site.register(PackagingRun)
admin.site.register(CanningQC)
admin.site.register(Staff)


