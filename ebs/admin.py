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
admin.site.register(Partner)
admin.site.register(Facility)
admin.site.register(Tank)
admin.site.register(Originator)
admin.site.register(Material)
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


